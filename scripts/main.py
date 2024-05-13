import click
from dotenv import load_dotenv

from app.daily_news.service import collect_news

load_dotenv()


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
    click.echo(result)


cli.add_command(collect)

if __name__ == '__main__':
    cli()
