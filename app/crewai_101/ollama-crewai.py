from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama

llm = Ollama(model="crewai-llama3", base_url="http://192.168.1.108:11434")

general_agent = Agent(role="Math Professor",
                      goal="""Provide the solution to the students that are asking mathematical questions and give 
                      them the answer.""",
                      backstory="""You are an excellent math professor that likes to solve math questions in a way 
                      that everyone can understand your solution""",
                      allow_delegation=False,
                      verbose=True,
                      llm=llm
                      )
task = Task(
    description="""what is 3 + 5""",
    expected_output="a text explaining the sum of the two num",
    agent=general_agent
)

crew = Crew(
    agents=[general_agent],
    tasks=[task],
)

if __name__ == '__main__':
    result = crew.kickoff()
    print(result)
