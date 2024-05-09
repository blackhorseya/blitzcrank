from crewai import Crew, Process
from dotenv import load_dotenv

from agents import Agents
from tasks import Tasks

load_dotenv()

topic = 'software engineering'

agents = Agents()
tasks = Tasks()

news_collector = agents.collector_agent(topic)
content_organizer = agents.organizer_agent()
markdown_generator = agents.generator_agent()

fetch_news_task = tasks.fetch_news_task(news_collector, topic)
organize_data_task = tasks.organize_data_task(content_organizer)
generate_markdown_task = tasks.generate_markdown_task(markdown_generator)

# Initialize the Crew with the News Collector Agent
crew = Crew(
    name='Daily Tech News Crew',
    agents=[news_collector, content_organizer, markdown_generator],
    tasks=[fetch_news_task, organize_data_task, generate_markdown_task],
    verbose=True,
    memory=True,
)

if __name__ == '__main__':
    # Starting the task execution process with enhanced feedback
    result = crew.kickoff()
