from dotenv import load_dotenv
import openai
import os
from run_command import run_command

load_dotenv()

#prompt = 'escribe dos comandos, uno que crea un archivo text.txt en el desktop y luego otro que crea un archivo elias.txt en el desktop'

def command_writer(prompt):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    messages = [
        {
            "role": "user",
            "content": f"{prompt} (Note: Generate a Linux Ubuntu terminal commands based on this prompt. Do not write anything else besides the command terminal lines for Linux Ubuntu. All the commands are always made from the same directory. So if you are going to change directory you have to change for every command. You should specify the directory in each command. The commands you are writing will be run just as you are writing them. When you are writing you respose each command should go on one separate line. Never put two commands on the same line, and never leave empty lines. The codes will be run line by line.)"
        }
    ]
    
    second_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        api_key=OPENAI_API_KEY
    )
    
    # Extract the content from the response
    terminal_prompts_str = second_response['choices'][0]['message']['content']
    
    # Split the content into lines and store each line as an item in a list
    terminal_prompts = terminal_prompts_str.strip().split('\n')
    
    #print(terminal_prompts)
   # print("Type:", type(terminal_prompts))
    
    for command in terminal_prompts:
        print(f"Executing command: {command}")
     #   run_command(prompt, [command])

    # Run each command line by line
    run_command(prompt, terminal_prompts)

#command_writer(prompt)
