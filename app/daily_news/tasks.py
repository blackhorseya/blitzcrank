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
                f""" Using the articles collected, perform a detailed analysis to identify key themes, trends, 
                and statistical data. Extract important points such as technological advancements, market impacts, 
                and expert opinions. Summarize these insights to prepare for effective reporting.
                
                {self.__tip_section()}
                """
            ),
            expected_output=dedent(
                f"""A structured document containing summarized points from each article, including key data and 
                trends identified during the analysis. This document should organize information in a way that 
                highlights the most critical insights for easy reference in the next task."""
            ),
            agent=agent,
            tools=[],
        )

    def generate_markdown_task(self, agent: Agent) -> Task:
        return Task(
            description=dedent(
                f"""Compile the insights from the analysis into a cohesive and engaging markdown report. Structure 
                the document to include an introduction, detailed sections on each key finding, and a conclusive 
                summary. Use markdown formatting to enhance readability and professional presentation.
                
                {self.__tip_section()}
                """
            ),
            expected_output=dedent(
                """A markdown file that effectively communicates the findings from the analysis. The report should be 
                clear, well-structured, and ready for publication or internal distribution. Include headings, 
                bullet points, and any necessary code snippets or data visualizations to support the text."""
            ),
            output_file=f'{datetime.now().strftime("%Y-%m-%d")}.md',
            agent=agent,
            tools=[],
        )
