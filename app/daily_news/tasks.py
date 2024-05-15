from datetime import datetime
from textwrap import dedent

from crewai import Agent, Task

from app.daily_news.tools.markdown import MarkdownFormatter


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
                f"""
                A list of URLs, each pointing to a news article relevant to the specified topic. The list should  
                be comprehensive and up-to-date, ensuring a broad coverage of the {topic} from various perspectives."""
            ),
            agent=agent,
            tools=[],
        )

    def organize_data_task(self, agent: Agent, topic: str) -> Task:
        return Task(
            description=dedent(
                f"""
                You need to collect and analyze the latest technology news about {topic}. 
                Please focus on identifying major trends, emerging technologies, and market impacts.
                
                Your final output should be a detailed news list that must include for each article:
                
                1. Title: The article title
                2. Summary: A brief summary
                3. Link: A URL to the original article
                4. Comment: A professional comment on the article
                
                {self.__tip_section()}
                """
            ),
            expected_output=dedent(
                f"""A list of the latest technology news summaries and related links."""
            ),
            agent=agent,
            tools=[],
        )

    def generate_markdown_task(self, agent: Agent) -> Task:
        return Task(
            description=dedent(
                f"""
                Use the MarkdownGenerator tool to convert the collected news data into a Markdown formatted document.
                Ensure the document includes titles, summaries, and source links for each news item.
                
                {self.__tip_section()}
                """
            ),
            expected_output=dedent(
                """A Markdown formatted file with the latest tech news."""
            ),
            output_file=f'{datetime.now().strftime("%Y-%m-%d")}.md',
            agent=agent,
            tools=[MarkdownFormatter()],
        )
