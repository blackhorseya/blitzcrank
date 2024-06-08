import os
from crewai import Agent, Crew, Process, Task
from crewai_tools import BaseTool

# 定义自定义工具，用于读取 Markdown 文件
class MarkdownReaderTool(BaseTool):
    name: str = "MarkdownReader"
    description: str = "Reads content from a specified markdown file."

    def _run(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            return f"Error: The file at {file_path} was not found."
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except Exception as e:
            return f"An error occurred while reading the file: {e}"

# 定义一个包含提示信息的函数
def __tip_section():
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"

# 初始化自定义工具
markdown_reader = MarkdownReaderTool()

# 创建技术专家代理
tech_expert = Agent(
    role='Tech Expert',
    goal='Read and analyze the notes from a markdown file {file_path} and provide a comprehensive analysis and explanation.',
    verbose=True,
    memory=True,
    backstory=(
        "With a deep understanding of technology and innovation, you analyze complex technical concepts and summarize them into clear, "
        "concise key points and information. You have years of experience in the tech industry and a knack for identifying critical details."
    ),
    tools=[markdown_reader],
    allow_delegation=False
)

# 创建写手代理，能够生成完整的博客文章
writer = Agent(
    role='Writer',
    goal='Rewrite the blog post based on the comprehensive analysis provided by the tech expert, including title, subtitle, content, code examples, and tags.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner. You have a passion for writing and a deep understanding of multiple subjects."
    ),
    tools=[markdown_reader],
    allow_delegation=False
)

# 创建技术分析任务
tech_analysis_task = Task(
    description=(
            "Read the notes from the provided markdown file and provide a comprehensive analysis and explanation. The analysis should include the following sections:\n"
            "- Key Points: Highlight the main points and concepts discussed in the notes\n"
            "- Detailed Information: Provide detailed information and explanations for each key point\n"
            "- Explanation of Design Principles: Explain the design principles and concepts mentioned in the notes\n"
            "- Relevant Examples or Case Studies: Include relevant examples or case studies to illustrate the points\n"
            "- Conclusion: Summarize the findings and discuss the implications\n"
            + __tip_section()
    ),
    expected_output='A comprehensive analysis of the notes, including key points, detailed information, explanations of design principles, examples, and conclusion.',
    tools=[markdown_reader],
    agent=tech_expert,
    async_execution=False,
    output_file='testdata/tech-analysis.md',
    timeout=1800,  # 设置超时时间为30分钟
    human_input=True  # 需要人类输入以监督任务
)

# 创建内容创作任务，要求重新撰写博客文章
content_creation_task = Task(
    description=(
            "Read the comprehensive analysis from the tech expert (testdata/tech-analysis.md) and rewrite the blog post. The post should include a compelling title, a relevant "
            "subtitle, appropriate tags, and ensure the inclusion of code examples where relevant. The blog post should cover the following sections:\n"
            "- Title: A compelling title that summarizes the blog post\n"
            "- Subtitle: A relevant subtitle that provides additional background information or an overview of the content\n"
            "- Introduction: Brief introduction to the topic\n"
            "- Subsections: Relevant subsections that break down the content into sections\n"
            "- Content: Engaging and informative content based on the comprehensive analysis, including examples and detailed analysis\n"
            "- Code Examples: Include relevant code examples to illustrate key points\n"
            "- Tags: Include appropriate tags for the blog post\n"
            "- Conclusion: Summarize the findings and provide a closing thought\n"
            + __tip_section()
    ),
    expected_output=(
        "A professional blog post with the following structure:\n"
        "- Title: A compelling title that summarizes the blog post\n"
        "- Subtitle: A relevant subtitle that provides additional background information or an overview of the content\n"
        "- Introduction: Brief introduction to the topic\n"
        "- Subsections: Relevant subsections that break down the content\n"
        "- Content: Engaging and informative content based on the comprehensive analysis, including examples and detailed analysis\n"
        "- Code Examples: Include relevant code examples to illustrate key points\n"
        "- Tags: Appropriate tags for the blog post\n"
        "- Conclusion: Summarize the findings and provide a closing thought"
    ),
    tools=[markdown_reader],
    agent=writer,
    async_execution=False,
    output_file='testdata/professional-blog-post.md',
    timeout=1800,  # 设置超时时间为30分钟
    human_input=True  # 需要人类输入以监督任务
)

# 创建包含技术专家代理和写手代理的团队
crew = Crew(
    agents=[tech_expert, writer],
    tasks=[tech_analysis_task, content_creation_task],
    process=Process.sequential
)

if __name__ == '__main__':
    # 提供 Markdown 文件的路径
    inputs = {'file_path': 'testdata/notes.md'}  # 确保这个路径是正确的
    result = crew.kickoff(inputs=inputs)
    print(result)
