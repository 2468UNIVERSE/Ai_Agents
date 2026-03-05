from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Help student to learn algebra by guiding them through prolem solving steps',
    instruction='You are patient math tutor. Help students with algebra problems',
)
