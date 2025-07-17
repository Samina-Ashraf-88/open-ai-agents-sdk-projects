from agents import Agent
from tools.travel_tools import get_flights, suggest_hotels

BookingAgent = Agent(
    name="BookingAgent",
    instructions="Help users book flights and hotels using available tools.",
    tools=[get_flights, suggest_hotels],
)
DestinationAgent = Agent(
    name="DestinationAgent",
    instructions="Suggest travel destinations based on user's interests or mood.",
)
ExploreAgent = Agent(
    name="ExploreAgent",
    instructions="Suggest local attractions and foods for the destination.",
)
