import asyncio
from openai_response import run_conversation

async def input_prompt():
    while True:
        prompt = input("Please enter your text: ")
        await run_conversation(prompt)

if __name__ == "__main__":
    asyncio.run(input_prompt())