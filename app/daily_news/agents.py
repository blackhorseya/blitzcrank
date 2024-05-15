import os
from textwrap import dedent

from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_community.llms import Ollama


class Agents:
    def __init__(self):
        self.Ollama = Ollama(model=os.getenv("OLLAMA_MODEL"), base_url=os.getenv("OLLAMA_BASE_URL"))

    def collector_agent(self, topic: str, verbose: bool) -> Agent:
        return Agent(
            role='Technology News Harvester',
            goal=f'Collect daily technology news from various sources on {topic}.',
            backstory=dedent(
                f"""As a digital news hound, your circuits buzz with activity at the mere mention of new 
                developments. Eager to fetch the freshest information, you sift through the digital expanse, 
                always on the hunt for the most relevant articles and insights."""
            ),
            tools=[SerperDevTool()],
            memory=True,
            allow_delegation=False,
            verbose=verbose,
            llm=self.Ollama,
        )

    def organizer_agent(self, verbose: bool) -> Agent:
        return Agent(
            role='Technology Analyst',
            goal='Extract and analyze key data from textual content to identify trends and insights',
            backstory=dedent(
                """As an Analyst, you are skilled in navigating through large volumes of text and distilling the 
                essence of information. Your expertise helps in uncovering valuable insights from diverse sources."""
            ),
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            memory=True,
            allow_delegation=False,
            verbose=verbose,
            llm=self.Ollama,
        )

    def generator_agent(self, verbose: bool) -> Agent:
        return Agent(
            role='Report Generator',
            goal='Generate a markdown report from the analyzed news',
            backstory=dedent(
                "A master of words and a craftsman of data, you transform complex analyses into clear,"
                " comprehensible markdown reports. Your goal is to communicate effectively, ensuring"
                " that insights are not only gathered but shared in an engaging and accessible way."
            ),
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            memory=True,
            allow_delegation=False,
            verbose=verbose,
            llm=self.Ollama,
        )
