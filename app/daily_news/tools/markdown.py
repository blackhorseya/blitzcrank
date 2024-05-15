from crewai_tools import BaseTool


class MarkdownFormatter(BaseTool):
    name: str = "MarkdownGenerator"
    description: str = "Converts a list of news items into a formatted Markdown document."

    def _run(self, news_items: list) -> str:
        # 开始Markdown文档
        markdown_text = "# Daily Tech News Digest\n\n"

        # 为每个新闻项添加Markdown格式的段落
        for item in news_items:
            title = item['title']
            summary = item['summary']
            link = item['link']

            markdown_text += f"## {title}\n\n"  # 标题
            markdown_text += f"{summary}\n\n"  # 摘要
            markdown_text += f"[Read more]({link})\n\n"  # 链接

        return markdown_text
