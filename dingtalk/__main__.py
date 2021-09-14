"""Console script for dingtalk."""
import sys

import click

from dingtalk.dingtalk import DingTalk


@click.command()
def main():
    """Console script for dingtalk."""
    access = '6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfc5ed89'
    secret = '0ed50da84fca5e37491b032a660dcfd2fd6aef8e2dcb74caa39ddb434421ad78'
    client = DingTalk(access=access, secret=secret, pc_slide=False, fail_notice=False)
    result = client.text(**dict(at_all=True, msg='哈哈'))

    click.echo(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
