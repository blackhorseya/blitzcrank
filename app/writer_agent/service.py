import os
from crewai import Agent, Crew, Process, Task
from crewai_tools import BaseTool

# 定義自定義工具，用於讀取 Markdown 文件
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

# 初始化自定義工具
markdown_reader = MarkdownReaderTool()

# 創建技術專家代理
tech_expert = Agent(
    role='Tech Expert',
    goal='Analyze the notes from a markdown file {file_path} and write a comprehensive blog post.',
    verbose=True,
    memory=True,
    backstory=(
        "With a deep understanding of technology and innovation, you analyze complex technical concepts and present them in an"
        "engaging and accessible manner. You have years of experience in the tech industry and a knack for explaining intricate ideas clearly."
    ),
    tools=[markdown_reader],
    allow_delegation=False
)

# 創建寫手代理，能夠生成完整的博客文章
writer = Agent(
    role='Writer',
    goal='Create a professional blog post based on notes from a markdown file, including title, subtitles, and tags.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner. You have a passion for writing and a deep understanding of multiple subjects."
    ),
    tools=[markdown_reader],
    allow_delegation=False
)

# 創建技術分析任務
tech_analysis_task = Task(
    description=(
        "Read the notes from the provided markdown file and write a comprehensive blog post. The post should be well-structured, engaging,"
        "and provide in-depth technical analysis. Ensure to include the following sections:\n"
        "- Introduction: Provide a brief overview of the topic\n"
        "- Key Points: Highlight the main points and concepts discussed in the notes\n"
        "- Detailed Analysis: Expand on the key points with in-depth analysis, examples, and explanations\n"
        "- Case Studies or Examples: Include relevant case studies or practical examples to illustrate the points\n"
        "- Conclusion: Summarize the findings and discuss the implications"
    ),
    expected_output='A detailed and well-structured blog post based on the provided notes, including introduction, key points, detailed analysis, examples, and conclusion.',
    tools=[markdown_reader],
    agent=tech_expert,
    async_execution=False,
    output_file='testdata/tech-blog-post.md',
    timeout=1800  # 設置超時時間為30分鐘
)

# 創建內容創作任務，要求生成完整的博客文章
content_creation_task = Task(
    description=(
        "Read the detailed tech blog post from the file (testdata/tech-blog-post.md) and create a professional blog post. The post should include a compelling title, relevant"
        "subtitles, and appropriate tags. Ensure the content is well-structured, engaging, and easy to understand. The blog post should cover the following sections:\n"
        "- Title: A compelling title that summarizes the blog post\n"
        "- Introduction: Brief introduction to the topic\n"
        "- Subtitles: Relevant subtitles that break down the content into sections\n"
        "- Content: Engaging and informative content based on the provided notes, including examples and detailed analysis\n"
        "- Tags: Appropriate tags for the blog post\n"
        "- Conclusion: Summarize the findings and provide a closing thought"
    ),
    expected_output=(
        "A professional blog post with the following structure:\n"
        "- Title: A compelling title that summarizes the blog post\n"
        "- Introduction: Brief introduction to the topic\n"
        "- Subtitles: Relevant subtitles that break down the content\n"
        "- Content: Engaging and informative content based on the provided notes, including examples and detailed analysis\n"
        "- Tags: Appropriate tags for the blog post\n"
        "- Conclusion: Summarize the findings and provide a closing thought"
    ),
    tools=[markdown_reader],
    agent=writer,
    async_execution=False,
    output_file='testdata/professional-blog-post.md',
    timeout=1800  # 設置超時時間為30分鐘
)

# 創建包含技術專家代理和寫手代理的團隊
crew = Crew(
    agents=[tech_expert, writer],
    tasks=[tech_analysis_task, content_creation_task],
    process=Process.sequential
)

if __name__ == '__main__':
    # 提供 Markdown 文件的路徑
    inputs = {'file_path': 'testdata/notes.md'}  # 確保這個路徑是正確的
    result = crew.kickoff(inputs=inputs)
    print(result)
