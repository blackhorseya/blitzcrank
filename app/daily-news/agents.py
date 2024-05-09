import os
from textwrap import dedent

from crewai import Agent
from crewai_tools import SerperDevTool
from langchain.llms import Ollama

search_tool = SerperDevTool()


class Agents:
    def __init__(self):
        self.Ollama = Ollama(model="llama3", base_url=os.getenv("OLLAMA_BASE_URL"))

    def collector_agent(self, topic: str) -> Agent:
        return Agent(
            role='Technology News Harvester',
            goal=f'Collect daily technology news from various sources on {topic}.',
            backstory=dedent(
                """With a keen eye for detail, you're always on the lookout for the latest news and trends in the 
                tech industry. Your goal is to keep up with the latest developments and share them with the world."""
            ),
            tools=[search_tool],
            allow_delegation=True,
            llm=self.Ollama,
        )

    def organizer_agent(self) -> Agent:
        pass

    def generator_agent(self) -> Agent:
        pass
