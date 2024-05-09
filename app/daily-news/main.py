import os

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

from agents import Agents
from tasks import Tasks

load_dotenv()

search_tool = SerperDevTool()

os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

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
    allow_delegation=True,
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

# Creating the Content Organizer Agent with memory and verbose mode
content_organizer = Agent(
    role='Content Organizer',
    goal='Organize raw news data into structured format.',
    verbose=True,
    memory=True,
    backstory=(
        "With a knack for structuring information, you excel at organizing raw data into meaningful insights."
        "Your goal is to extract key details from the news articles and present them in a structured format."
    ),
    allow_delegation=True,
)

# Task for organizing data from raw news articles
organize_data_task = Task(
    description=(
        "Organize the raw news data into a structured format."
        "Focus on extracting the headline, date, author, and summary of each news article."
        "Present the organized data in a clear and concise manner."
    ),
    expected_output='A structured dataset containing the headline, date, author, and summary of each news article.',
    tools=[],
    agent=content_organizer,
)

# Creating the Markdown Generator Agent
markdown_generator = Agent(
    role='Report Compiler',
    goal='Generate a Markdown file from organized news data.',
    backstory=(
        "With a talent for storytelling, you excel at transforming raw data into engaging narratives."
        "Your goal is to compile the organized news data into a Markdown file for easy consumption."
    ),
    allow_delegation=True,
)

# Task to generate Markdown
generate_markdown_task = Task(
    description='Convert organized data into Markdown format.',
    agent=markdown_generator,
    expected_output='Markdown file',
    output_file='tech_news_report.md'
)

agents = Agents()
tasks = Tasks()

# Initialize the Crew with the News Collector Agent
crew = Crew(
    name='Daily Tech News Crew',
    agents=[news_collector, content_organizer, markdown_generator],
    tasks=[fetch_news_task, organize_data_task, generate_markdown_task],
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
