import asyncio
import os
from openai import AsyncOpenAI
from agents import Agent,OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv
load_dotenv()


gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    agent = Agent(
        name="Assistant",instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="gemini-2.5-pro", openai_client=client),
    )
    result = await Runner.run(
        agent,"Tell me about recursion in programming.",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())