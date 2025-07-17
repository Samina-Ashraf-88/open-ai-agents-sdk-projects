import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from tools import get_career_roadmap, get_real_world_jobs
from agents import OpenAIChatCompletionsModel, Runner, set_tracing_disabled, Agent
from agentic import CareerAgent, SkillAgent, JobAgent
load_dotenv()

gemini_api_key =os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_tracing_disabled(disabled=True)
    
mentor_agent = Agent(
    name="CareerMentorAgent",
    instructions="Help students explore careers, skills, and job roles.",
    handoffs=[CareerAgent, SkillAgent, JobAgent],
    tools=[get_career_roadmap, get_real_world_jobs],
    model=OpenAIChatCompletionsModel(model="gemini-2.5-pro", openai_client=client),
    )
    
async def main():
    print("Career Mentor Agent is ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = await Runner.run(mentor_agent, user_input)
        print("Agent:", result.final_output)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            task = loop.create_task(main())
        else:
            loop.run_until_complete(main())
    except RuntimeError:
        asyncio.run(main())