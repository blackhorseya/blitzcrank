import os

import click
from dotenv import load_dotenv

from app.daily_news.service import collect_news

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")


@click.group()
def cli():
    """Simple CLI for the program."""
    pass


@click.command()
@click.argument('topic', required=True)
@click.option('--verbose', is_flag=True, help='Enable verbose mode.', default=True)
def collect(topic: str, verbose: bool):
    """
    Collects news on the given topic.
    :param topic:
    :param verbose:
    """
    result = collect_news(topic, verbose=verbose)

    # file_name = f"{datetime.now().strftime('%Y-%m-%d')}.md"
    # with open(file_name, "rb") as file:
    #     content = file.read()
    #
    # # upload the markdown file to the GitHub repository
    # print(upload_to_github(repo="blackhorseya/note1", path=f"4. Archives/news/{file_name}",
    #                        token=github_token, content=content, commit_message="Updated via API"))

    click.echo(result)


@click.command()
def rewrite():
    """
    Rewrite the post.
    :return:
    """
    pass


cli.add_command(collect)
cli.add_command(rewrite)

if __name__ == '__main__':
    cli()
