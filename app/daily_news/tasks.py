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
                你需要收集和分析關於{topic}的最新技术新闻。
                请专注于识别主要的趋势，新兴的技术，以及市场的影响。
                
                你的最终输出应该是一个详细的新闻列表，必須包括每篇文章的
                1. title: 文章标题
                2. summary: 一段摘要
                3. link: 一個指向原始文章的URL
                4. comment: 對這篇文章的專業評論
                
                {self.__tip_section()}
                """
            ),
            expected_output=dedent(
                f"""一个包含最新技术新闻摘要和相关链接的列表。"""
            ),
            agent=agent,
            tools=[],
        )

    def generate_markdown_task(self, agent: Agent) -> Task:
        return Task(
            description=dedent(
                f"""
                根据收集的技术新闻信息和给定的Markdown模板，撰写一份报告。
                请确保报告格式正确，并且语言通顺易懂。
                
                {self.__tip_section()}
                """
            ),
            expected_output=dedent(
                """一份格式化为Markdown的技术新闻报告文件。"""
            ),
            output_file=f'{datetime.now().strftime("%Y-%m-%d")}.md',
            agent=agent,
            tools=[MarkdownFormatter()],
        )
