import json
import click
from .utils import formatter


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--sort', '-s', is_flag=True)
def main(path, sort):
    with open(path, 'r') as _f:
        click.secho(
            formatter(_f.read(), sort_keys=sort),
            fg='yellow', bold=True
        )


if __name__ == '__main__':
    main()


