import os
from textwrap import dedent

from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama

search_tool = SerperDevTool()


class Agents:
    def __init__(self):
        self.Ollama = Ollama(model=os.getenv("OLLAMA_MODEL"), base_url=os.getenv("OLLAMA_BASE_URL"))

    def collector_agent(self, topic: str) -> Agent:
        return Agent(
            role='Technology News Harvester',
            goal=f'Collect daily technology news from various sources on {topic}.',
            backstory=dedent(
                f"""
                With a keen eye for detail, you're always on the lookout for the latest news and trends in the 
                tech industry. 
                Your goal is to keep up with the latest developments and share them with the world.
                """
            ),
            tools=[search_tool],
            # llm=self.Ollama,
        )

    def organizer_agent(self) -> Agent:
        return Agent(
            role='Content Organizer',
            goal='Organize raw news data into structured format.',
            backstory=dedent(
                """
                With a knack for structuring information, you excel at organizing raw data into meaningful insights. 
                Your goal is to extract key details from the news articles and present them in a structured format.
                """
            ),
            # llm=self.Ollama,
        )

    def generator_agent(self) -> Agent:
        return Agent(
            role='Report Compiler',
            goal='Generate a Markdown file from organized news data.',
            backstory=dedent(
                """With a talent for storytelling, you excel at transforming raw data into engaging narratives. Your 
                goal is to compile the organized news data into a Markdown file for easy consumption."""
            ),
            # llm=self.Ollama,
        )
