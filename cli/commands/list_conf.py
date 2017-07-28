import click
from cli.cli import pass_context
from cli import setting


@click.command('list_conf', short_help='Show global configuration')
@pass_context
def cli(ctx):
    setting.display(ctx)
