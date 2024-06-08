import os

from crewai import Agent, Crew, Process, Task
from crewai_tools import BaseTool


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


# Initialize the custom tool
markdown_reader = MarkdownReaderTool()

# Create the tech expert agent with enhanced capabilities
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

# Create the writer agent with a broader goal and memory capabilities
writer = Agent(
    role='Writer',
    goal='Create engaging and informative content based on various sources including markdown files.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner. You have a passion for writing and a deep understanding of multiple subjects."
    ),
    tools=[markdown_reader],
    allow_delegation=False
)

# Create a detailed writing task
tech_analysis_task = Task(
    description=(
        "Read the notes from the provided markdown file and write a comprehensive blog post. The post should be well-structured, engaging,"
        "and provide in-depth technical analysis. Make sure to include all the important points from the notes and expand on any complex topics."
    ),
    expected_output='A detailed and well-structured blog post based on the provided notes.',
    tools=[markdown_reader],
    agent=tech_expert,
    async_execution=False,
    output_file='tech-blog-post.md',
    timeout=1800  # Set a timeout of 30 minutes
)

# Create another task for the writer agent
content_creation_task = Task(
    description=(
        "Use the information from the markdown file (tech-blog-post.md) and other available sources to write an engaging and informative article. The article"
        "should be easy to understand, cover all important points, and be formatted appropriately for a blog post."
    ),
    expected_output='An engaging and informative blog article based on the provided notes.',
    tools=[markdown_reader],
    agent=writer,
    async_execution=False,
    output_file='engaging-blog-article.md',
    timeout=1800  # Set a timeout of 30 minutes
)

# Form the crew with the tech expert agent and writing task
crew = Crew(
    agents=[tech_expert, writer],
    tasks=[tech_analysis_task, content_creation_task],
    process=Process.sequential
)

if __name__ == '__main__':
    # Provide the path to the markdown file
    inputs = {'file_path': 'notes.md'}  # Ensure this path is correct
    result = crew.kickoff(inputs=inputs)
    print(result)
