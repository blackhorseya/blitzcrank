from crewai_tools import tool


class MarkdownTool:
    def __init__(self):
        self.name = 'MarkdownTool'
        self.description = 'A tool to generate markdown reports from text data.'

    @tool("markdown generator")
    def generate_markdown(data: str) -> str:
        """
        Generate a markdown report from the given text data.

        Args:
            data (str): The text data to be converted to markdown.

        Returns:
            str: The markdown formatted text.
        """
        return data
