# Merlin Terminal Assistant

Merlin is a terminal-based AI assistant that can answer questions and execute system commands. It uses OpenAI's GPT-4 model to understand and respond to user queries, and can perform various tasks including file operations and launching applications.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Ubuntu (or another Linux distribution)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/eliastsoukatos/merlin_terminal_assistant.git
   cd merlin-terminal-assistant
   ```

2. Set up a virtual environment:
   ```
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key to the file:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Activate the virtual environment (if not already activated):
   ```
   source myenv/bin/activate
   ```

2. Run the main script:
   ```
   python3 main.py
   ```

3. Enter your queries or commands when prompted.

## Features

- Natural language understanding: Ask questions or give commands in plain English.
- System command execution: The assistant can run system commands on your behalf.
- Background task handling: Can launch applications like web browsers without blocking the input.
- Directory management: Keeps track of important directories for easy access.

## File Structure

- `main.py`: The entry point of the application.
- `openai_response.py`: Handles communication with the OpenAI API.
- `command_executor.py`: Manages the execution of system commands.
- `directory_manager.py`: Keeps track of important directories.

## Troubleshooting

If you encounter any issues:

1. Ensure your virtual environment is activated.
2. Verify that all dependencies are installed correctly.
3. Check that your OpenAI API key is set correctly in the `.env` file.
4. If you encounter permission issues when running commands, ensure the assistant has the necessary permissions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]

## Disclaimer

This project uses the OpenAI API. Ensure you comply with OpenAI's use-case policy and terms of service when using this assistant.