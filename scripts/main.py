import click


@click.group()
def cli():
    """Simple CLI for the program."""
    pass


@click.command()
@click.argument('topic', required=True)
@click.option('--verbose', is_flag=False, help='Enable verbose mode.')
def collect(topic: str, verbose: bool):
    """Collect news on a specific topic."""
    if verbose:
        print(f'Collecting news on the {topic}...')


if __name__ == '__main__':
    cli()
