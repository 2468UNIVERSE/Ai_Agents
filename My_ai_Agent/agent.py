# this is the approach to to define the main section 

# from google.adk.agents.llm_agent import Agent

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='Help student to learn algebra by guiding them through prolem solving steps',
#     instruction='You are patient math tutor. Help students with algebra problems',
# )


# adk web to check for quick testing the application 
# adk api_server for the rest api
# programetical approach for the custom working to define the working of the ai agent as per the need
# *********************************************  complete basic code for the same  **********************************

#  Running the adk agent programatically
# importing all the required libraries
import asyncio
from dotenv import load_dotenv
import os
from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

load_dotenv()

# Define your agent 
agent = Agent(
    model='gemini-2.5-flash',
    name = 'math_tutor',
    instruction="""You are a patient math tutor.
    Guide students through problems step-by-step.
    Don't just give answeres - help them to discover solutions."""
)

# set up session and runner
APP_NAME = "math_tutor_app"
USER_ID = "student_1"
SESSION_ID = 'session_001'

session_service = InMemorySessionService()
runner = Runner(
    agent = agent,
    app_name = APP_NAME,
    session_service = session_service
)

# defining async function to run the agent
async def run_agent():
    # create session
    session = await session_service.create_session(
        app_name = APP_NAME,
        user_id= USER_ID,
        session_id = SESSION_ID
    )

    print(f"Session created: {SESSION_ID}\n")

    # prepare user message
    query = input("Enter your wuery:")
    user_message = Content(
        role="user",
        parts=[Part(text=query)]
    )

    # run agent and collect response
    print(f"User: {query}\n")
    print("Agent: ",end="")

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message
    ):
        # print final response
        if event.is_final_response() and event.content and event.content.parts:
            print(event.content.parts[0].text)

# run the agent 
# for jupyter notebook 
# await run_agent()

# for python scripts: use asyncio.run()
asyncio.run(run_agent())
