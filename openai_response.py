from dotenv import load_dotenv
import os
from openai import OpenAI
#Testing
from command_writer import command_writer


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


#Testing
#prompt = "Porfa lista todos los archivos en el formulario /home/eliastsoukatos/Documents/Python/Merlin/terminal_manager/"

#Testing
#def command_writer(prompt):
#    print("Executing function command_writer with the following JS code:")



additional_message_content = "Eres un asistente virtual que respondes todas mis preguntas, pero si detectas que te estoy pidiendo algo que requiere correr un comando en el terminal, llama a la función command_writer."

def run_conversation(prompt):
    messages = [{"role": "user", "content": prompt}]

    messages = [
        {"role": "user", "content": additional_message_content},
        {"role": "user", "content": prompt}
    ]

    tools = [
        {
            "type": "function",
            "function": {
            "name": "command_writer",
            "description": "Writes a terminal command based on the user input",
            "parameters": {},
                "required": [],
            },
            }  
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto", 

    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls


    if tool_calls:
        for tool_call in tool_calls:
            function_name = tool_call.function.name
 
            if function_name == "command_writer":
                command_writer(prompt)
    else:
        print(response.choices[0].message.content)


#Testing
#run_conversation(prompt)



#No descomentar
#if __name__ == "__main__":
#    run_conversation(prompt)
