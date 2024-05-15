from datetime import datetime
from textwrap import dedent

from crewai import Agent, Task


class Tasks:
    @staticmethod
    def __tip_section():
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def fetch_news_task(self, agent: Agent, topic: str) -> Task:
        return Task(
            description=dedent(
                f"""
                As a News Collector, scour the internet for articles related to {topic}. Utilize advanced search 
                tools to filter through the noise and gather only the most relevant and recent articles. Focus on 
                reputable sources to ensure the quality of information."
                
                {self.__tip_section()}
                """
            ),
            expected_output=dedent(
                f"""A list of URLs, each pointing to a news article relevant to the specified topic. The list should  
                be comprehensive and up-to-date, ensuring a broad coverage of the {topic} from various perspectives."""
            ),
            agent=agent,
            tools=[],
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
            tools=[],
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
            output_file=f'{datetime.now().strftime("%Y-%m-%d")}.md',
            agent=agent,
            tools=[],
        )
