import os
import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from agents.run import RunConfig
from dotenv import load_dotenv
from agent import narrator_agent, monster_agent, item_agent

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

external_client = AsyncOpenAI(
       api_key= gemini_api_key,
       base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
   )

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider= external_client,
    tracing_disabled= True,
)

main_agent = Agent(
       name="MainAgent",
       instructions=(
           "You are the game master. Route player inputs to the appropriate agent: "
           "NarratorAgent for story progression or exploration, "
           "MonsterAgent for combat scenarios, "
           "ItemAgent for inventory or item-related actions. "
           "If unsure, use NarratorAgent."
       ),
       model = model,
       handoffs=[narrator_agent, monster_agent, item_agent]
   )

async def main():
       print("Welcome to the Fantasy Adventure Game!")
       print("Type 'explore', 'fight', 'check inventory', or 'quit' to play.")
       
       while True:
           player_input = input("\nWhat do you do? ").lower().strip()
           if player_input == "quit":
               print("Thanks for playing!")
               break
           result = await Runner.run(main_agent,player_input, run_config = config)
           print(result.final_output)

if __name__ == "__main__":
       asyncio.run(main())