from openai_response import run_conversation

def input_prompt():
    prompt = input("Please enter your text: ")
    run_conversation(prompt)
    input_prompt()

if __name__ == "__main__":
    input_prompt()