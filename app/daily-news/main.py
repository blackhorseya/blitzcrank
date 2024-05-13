from crewai import Crew, Process
from dotenv import load_dotenv

from agents import Agents
from tasks import Tasks

load_dotenv()

default_topic = 'software engineering'

agents = Agents()
tasks = Tasks()

news_collector = agents.collector_agent(default_topic)
content_organizer = agents.organizer_agent()
markdown_generator = agents.generator_agent()

fetch_news_task = tasks.fetch_news_task(news_collector, default_topic)
organize_data_task = tasks.organize_data_task(content_organizer)
generate_markdown_task = tasks.generate_markdown_task(markdown_generator)

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
)


def collect_news(topic: str) -> str:
    print(f'Collecting news on the {topic}...')

    return f'News collected on the {topic}.'


if __name__ == '__main__':
    # Starting the task execution process with enhanced feedback
    result = crew.kickoff()

    # Displaying the result of the task execution process
    print(result)
