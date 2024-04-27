from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

search_tool = SerperDevTool()

# Creating the News Collector Agent with memory and verbose mode
news_collector = Agent(
    role='Technology News Harvester',
    goal='Collect daily technology news from various sources on {topic}.',
    verbose=True,
    memory=True,
    backstory=(
        "With a keen eye for detail, you're always on the lookout for the latest news and trends in the tech industry."
        "Your goal is to keep up with the latest developments and share them with the world."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Task for the News Collector to fetch news articles
fetch_news_task = Task(
    description=(
        "Fetch the latest technology news articles related to {topic} from various sources."
        "Focus on the most recent news and summarize the key points in a single document."
    ),
    expected_output='A single document containing the latest technology news articles on {topic}.',
    tools=[search_tool],
    agent=news_collector,
)


# Initialize the Crew with the News Collector Agent
crew = Crew(
    name='Daily Tech News Crew',
    agents=[news_collector],
    tasks=[fetch_news_task],
    verbose=True,
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

if __name__ == '__main__':
    # Starting the task execution process with enhanced feedback
    result = crew.kickoff(inputs={'topic': 'software engineering'})
    print(result)
