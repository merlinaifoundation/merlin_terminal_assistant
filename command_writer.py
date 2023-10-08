from dotenv import load_dotenv
import openai
import os
from run_command import run_command

load_dotenv()

#prompt = 'Porfa lista todos los archivos en el formulario /home/eliastsoukatos/Documents/Python/Merlin/terminal_manager/'

def command_writer(prompt):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    messages = [
        {
            "role": "user",
            "content": f"{prompt} (Note: Generate a single Linux Ubuntu terminal command based on this prompt. Do not write anything that is not a single command terminal line for Linux Ubuntu. The command you are writing will be run just as you are writing it.)"
        }
    ]
    
    second_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        api_key=OPENAI_API_KEY
    )
    
    terminal_prompt = second_response['choices'][0]['message']['content']
    
    # Assuming the terminal command is the first line of the response
    terminal_prompt = terminal_prompt.split('\n')[0]
    
    print(terminal_prompt)
    
    run_command(prompt, terminal_prompt)

#command_writer(prompt)