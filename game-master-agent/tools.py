from agents import function_tool

@function_tool
def roll_dice(sides: int) -> int:
       import random
       return random.randint(1, sides)

@function_tool
def generate_event() -> str:
       import random
       events = [
           "You find a hidden treasure chest!",
           "A wild beast appears from the shadows!",
           "You discover a mysterious ancient rune."
       ]
       return random.choice(events)
