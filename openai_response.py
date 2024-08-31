import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from command_executor import execute_commands
from directory_manager import directory_manager

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def run_conversation(prompt):
    directory_info = directory_manager.get_all_directories()
    
    messages = [
        {"role": "system", "content": f"You are a virtual assistant that responds to questions and can execute terminal commands when necessary. You have access to the following directories:\n{directory_info}\nWhen referring to these directories in commands, use the full path."},
        {"role": "user", "content": prompt}
    ]

    tools = [
        {
            "type": "function",
            "function": {
                "name": "execute_commands",
                "description": "Executes terminal commands based on the user input",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "commands": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of terminal commands to execute"
                        }
                    },
                    "required": ["commands"]
                }
            }
        }
    ]

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message
    
    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            if tool_call.function.name == "execute_commands":
                commands = eval(tool_call.function.arguments)["commands"]
                output = await execute_commands(commands)
                messages.append({"role": "function", "name": "execute_commands", "content": output})
        
        final_response = await client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        print(final_response.choices[0].message.content)
    else:
        print(response_message.content)