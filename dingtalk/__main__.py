"""Console script for dingtalk."""
import sys

import click

from dingtalk.dingtalk import DingTalk


@click.command()
def main():
    """Console script for dingtalk."""
    client = DingTalk(access='6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfc5ed89', secret=None, pc_slide=False, fail_notice=False)
    result = client.text(**dict(at_all=True, msg='[监控]哈哈'))

    click.echo(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
