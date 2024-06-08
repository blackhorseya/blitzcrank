from crewai import Agent
from crewai import Crew, Process
from crewai import Task
from crewai_tools import BaseTool


class MarkdownReaderTool(BaseTool):
    name: str = "MarkdownReader"
    description: str = "Reads content from a specified markdown file."

    def _run(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content


# Initialize the custom tool
markdown_reader = MarkdownReaderTool()

# Create the writer agent
writer = Agent(
    role='Writer',
    goal='Write a complete blog post based on notes from a markdown file.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[markdown_reader],
    allow_delegation=False
)

write_task = Task(
    description=(
        "Read the notes from the provided markdown file and write a complete blog post."
        "The post should be well-structured, engaging, and easy to understand."
        "Make sure to include all the important points from the notes."
    ),
    expected_output='A fully formatted blog post based on the provided notes.',
    tools=[markdown_reader],
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'  # Specify the output file for the blog post
)

crew = Crew(
    agents=[writer],
    tasks=[write_task],
    process=Process.sequential
)

if __name__ == '__main__':
    # Provide the path to the markdown file
    inputs = {'file_path': 'notes.md'}
    result = crew.kickoff(inputs=inputs)
    print(result)
