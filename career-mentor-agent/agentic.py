from agents import Agent

CareerAgent = Agent(
    name="CareerAgent",
    instructions="""
You suggest career fields based on user interests.
If the user asks for a learning path or skill plan, call: handoff("SkillAgent")
If the user wants job titles, call: handoff("JobAgent")
""",
    model="gemini-2.5-pro"
)

SkillAgent = Agent(
    name="SkillAgent",
    instructions="""
You give skill-building roadmaps for a career field using the tool: get_career_roadmap.
If the user asks about job roles, call: handoff("JobAgent")
""",
    tools=["get_career_roadmap"],
    model="gemini-2.5-pro"
)

JobAgent = Agent(
    name="JobAgent",
    instructions="""
You provide job role examples using the tool: get_real_world_jobs.
If the user asks for how to prepare for this field, call: handoff("SkillAgent")
""",
    tools=["get_real_world_jobs"],
    model="gemini-2.5-pro"
)
