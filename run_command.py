import subprocess
from final_response import generate_final_response  # Importar la función desde final_response.py

def run_command(prompt, terminal_prompts):
    all_command_output = ""
    all_error_message = ""
    
    for terminal_prompt in terminal_prompts:
        completed_process = subprocess.run(terminal_prompt, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

        command_output = completed_process.stdout
        error_message = completed_process.stderr

        if command_output:
            command_output = command_output[-500:]  # Limiting the output to the last 500 characters
            all_command_output += command_output + "\n"
        elif not command_output and not error_message:
            all_command_output += "Comando ejecutado con éxito, pero no hay salida.\n"
        elif error_message:
            error_message = error_message[-500:]  # Limiting the error message to the last 500 characters
            all_error_message += error_message + "\n"
        else:
            all_command_output += "Comando fallido, pero no hay mensaje de error.\n"

    print("Output:", all_command_output)
    print("Error:", all_error_message)
    generate_final_response(prompt, terminal_prompts, all_command_output, all_error_message)

# Example usage
#prompt = ' '
#terminal_prompts = ['touch ~/Desktop/elias.txt', 'touch ~/Desktop/texto.txt']
#run_command(prompt, terminal_prompts)
