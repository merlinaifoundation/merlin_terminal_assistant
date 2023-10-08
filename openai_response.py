from dotenv import load_dotenv
import os
import openai
from command_writer import command_writer


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

#prompt = "Porfa lista todos los archivos en el formulario /home/eliastsoukatos/Documents/Python/Merlin/terminal_manager/"

#def command_writer(prompt):
#    print("Executing function command_writer with the following JS code:")
additional_message_content = "Eres un asistente virtual que respondes todas mis preguntas, pero si detectas que te estoy pidiendo algo que requiere correr un comando en el terminal, llama a la función command_writer."

def run_conversation(prompt):
    messages = [{"role": "user", "content": prompt}]

    messages = [
        {"role": "user", "content": additional_message_content},
        {"role": "user", "content": prompt}
    ]

    functions = [
        {
            "name": "command_writer",
            "description": "Writes a terminal command based on the user input",
            "parameters": {
                "type": "object",
                "properties": {}
            },
            "required": []
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto", 
    )

    response_choices = response['choices']
    if 'function_call' in response_choices[0]['message']:
        command_writer(prompt)
    else:
        print(response_choices[0]['message']['content'])

#if __name__ == "__main__":
#    run_conversation(prompt)
