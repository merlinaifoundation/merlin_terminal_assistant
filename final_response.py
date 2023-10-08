from dotenv import load_dotenv
import openai
import os

load_dotenv()

#prompt = 'Porfa lista todos los archivos en el formulario /home/eliastsoukatos/Documents/Python/Merlin/terminal_manager/'
#terminal_prompt = 'ls /home/eliastsoukatos/Documents/Python/Merlin/terminal_manager/'
#command_output = 'main.py'
#error_message = ''

def generate_final_response(prompt, terminal_prompts, full_output):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    messages = [
        {
            "role": "system",
            "content": "Soy un asistente virtual que ejecuta comandos en el terminal."
        },
        {
            "role": "user",
            "content": f"Prompt del usuario: {prompt}"
        },
        {
            "role": "system",
            "content": f"Comando ejecutado en el terminal: {terminal_prompts}"
        },
        {
            "role": "system",
            "content": f"Resultado del terminal: {full_output}"
        }
    ]
    
    last_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        api_key=OPENAI_API_KEY
    )
    
    print(last_response['choices'][0]['message']['content'])
    
    return last_response

#generate_final_response(prompt, terminal_prompt, full_output)
