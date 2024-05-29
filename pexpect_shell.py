import pexpect
from final_response import generate_final_response

# Global variable to store the child shell
child_shell = None

def execute_command(command):
    global child_shell
    result = ""

    try:
        if child_shell is None:
            # Spawn a new bash session if not already running
            child_shell = pexpect.spawn('bash', env={"TERM": "dumb"})
            child_shell.expect_exact('$ ')

        # Send the command
        child_shell.sendline(command)
        child_shell.expect_exact('$ ')
        output = child_shell.before.decode('utf-8').strip().split('\n')[1:-1]

        # Send the pwd command to get the current directory
        child_shell.sendline('pwd')
        child_shell.expect_exact('$ ')
        directory = child_shell.before.decode('utf-8').strip().split('\n')[1]

        # Append the directory and the output of the command to the result string
        result += "=== CURRENT DIRECTORY ===\n"
        result += directory + "\n"
        result += "\n=== OUTPUT ===\n"
        result += "\n".join(output) + "\n"

    except Exception as e:
        print(f"An error occurred: {e}")

    return result

def execute_commands_list(prompt, terminal_prompts):
    full_output = ""
    for command in terminal_prompts:
        print(f"Executing command: {command}")
        full_output += execute_command(command) + "\n"
    
    print(full_output)
    generate_final_response(prompt, terminal_prompts, full_output)
    return full_output



#Testing

# List of terminal commands to execute
#terminal_prompts = ['ls', 'pwd', 'echo Hello, World!']
#prompt = " "

# Call the function to execute all commands in the list and print the full output
#execute_commands_list(prompt, terminal_prompts)
