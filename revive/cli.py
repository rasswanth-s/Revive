import click

@click.command()
def revive():
    """Prints 'Hello, world!'."""
    print('Welcome to Revive!')

if __name__ == '__main__':
    revive()