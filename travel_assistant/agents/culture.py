from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import get_local_culture_info

local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-2.0-flash",
    description="Recommends local gastronomy, customs and useful phrases for travelers.",
    instruction="""
You are a local culture advisor for travelers.

Your task is to help travelers connect respectfully with local culture.

Use the available tool to retrieve gastronomy, customs and useful phrases for the destination.

Rules:
1. Present gastronomy recommendations clearly.
2. Explain customs with cultural sensitivity and respect.
3. List practical phrases the traveler can use.
4. Encourage travelers to learn a few local words as a sign of respect.
5. Keep the tone friendly and motivating.
""",
    tools=[get_local_culture_info],
)
