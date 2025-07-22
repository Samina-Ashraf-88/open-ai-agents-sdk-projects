Master Agent (Fantasy Adventure Game):
What It Does: Run a text-based adventure game using multiple AI agents:
● Narrates an adventure story based on player choices
● Uses Tool: roll_dice() and generate_event() to control game flow
● Hands off between:
○ NarratorAgent (story progress),
○ MonsterAgent (combat phase),
○ ItemAgent (inventory & rewards)
Uses:
● OpenAI Agent SDK + Runner
● Tools: Dice Roller, Event Generator
● Handoff: Dynamic switches between roles based on gameplay.
