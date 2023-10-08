import subprocess
from final_response import generate_final_response  # Importar la función desde final_response.py

#prompt = 'Porfa lista todos los archivos en el formulario /home/eliastsoukatos/Documents/Python/Merlin/terminal_manager/'
#terminal_prompt = 'ls /home/eliastsoukatos/Documents/Python/Merlin/terminal_manager/'

def run_command(prompt, terminal_prompt):
    completed_process = subprocess.run(terminal_prompt, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    
    command_output = completed_process.stdout
    error_message = completed_process.stderr
    
    if command_output:
        command_output = command_output[-500:]  # Limiting the output to the last 500 characters
    elif not command_output and not error_message:
        command_output = "Comando ejecutado con éxito, pero no hay salida."
    elif error_message:
        error_message = error_message[-500:]  # Limiting the error message to the last 500 characters
    else:
        command_output = "Comando fallido, pero no hay mensaje de error."
    
    
    print("Output:", command_output)
    print("Error:", error_message)
    # Llamar a la función generate_final_response con los argumentos necesarios
    generate_final_response(prompt, terminal_prompt, command_output, error_message)

#run_command(prompt, terminal_prompt)
