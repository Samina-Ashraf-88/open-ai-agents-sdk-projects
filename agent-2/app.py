import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-pro",
    openai_client=client
)
agent= Agent(name="study_agent", 
    instructions="""You are a study helper agent with 3 main functions:
1. Answer academic questions clearly and concisely.
2. Provide helpful study tips and motivation.
3. Summarize small text passages into key points.
Keep responses under 200 words.""",
    model=model)

user_question=input("Please enter your query:")

async def main():
    result = await Runner.run(agent,user_question)
    print("Agent:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
