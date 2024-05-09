from textwrap import dedent

from crewai import Agent, Task
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()


class Tasks:
    @staticmethod
    def __tip_section():
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def fetch_news_task(self, agent: Agent, topic: str) -> Task:
        return Task(
            description=dedent(
                f"""
                Fetch the latest technology news articles related to {topic} from various sources. 
                Focus on the most recent news and summarize the key points in a single document.
                
                {self.__tip_section()}
                """
            ),
            expected_output=f'A single document containing the latest technology news articles on {topic}.',
            tools=[search_tool],
            agent=agent,
        )

    def organize_data_task(self, agent: Agent) -> Task:
        return Task(
            description=dedent(
                f"""
                Organize the raw news data into a structured format. 
                Focus on extracting the headline, date, author, and summary of each news article. 
                Present the organized data in a clear and concise manner.
                
                {self.__tip_section()}
                """
            ),
            expected_output=dedent(
                f"""A structured dataset containing the headline, date, author, and summary of each news article."""
            ),
            agent=agent,
        )

    def generate_markdown_task(self, agent: Agent) -> Task:
        return Task(
            description=dedent(
                f"""
                Convert organized data into Markdown format.
                
                {self.__tip_section()}
                """
            ),
            expected_output='Markdown file',
            output_file='tech_news_report.md',
            agent=agent,
        )
