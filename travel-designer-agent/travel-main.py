
import os
import asyncio
from dotenv import load_dotenv
from openai import  AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel,Runner,set_tracing_disabled
from agent.agentic import DestinationAgent, ExploreAgent, BookingAgent
from tools.travel_tools import get_flights, suggest_hotels

load_dotenv()

gemini_api_key =os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
set_tracing_disabled(disabled=True)

main_agent = Agent(
    name="TravelDesignerAgent",
    model=OpenAIChatCompletionsModel(openai_client=client, model="gemini-2.5-pro"),
    instructions="You help users plan travel by suggesting destinations, booking travel, and recommending activities also keep taking instructions from the user until you are satisfied that you give complete answer.",
    tools=[get_flights, suggest_hotels],
    handoffs=[DestinationAgent, ExploreAgent, BookingAgent]
)
async def main():
    print("Travel Designer Agent is ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = await Runner.run(main_agent, user_input)
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