import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel
from tools import roll_dice, generate_event
from dotenv import load_dotenv

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

narrator_agent = Agent(
       name="NarratorAgent",
       instructions="Advance the story based on the player's input and event outcomes. Describe the scene vividly.",
       model= model,
       tools=[generate_event]
   )

monster_agent = Agent(
       name="MonsterAgent",
       instructions="Handle combat scenarios. Use roll_dice to determine attack success (6 or higher succeeds). Describe the fight.",
       model= model,
       tools=[roll_dice]
   )

item_agent = Agent(
       name="ItemAgent",
       instructions="Manage inventory and rewards. Describe items found and their effects.",
       model= model,
   )
