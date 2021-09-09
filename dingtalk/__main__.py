"""Console script for dingtalk."""
import sys

import click

from .dingtalk import DingTalk


@click.command()
def main(args=None):
    """Console script for dingtalk."""
    talk = DingTalk(access='6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfc5ed89', secret=None, pc_slide=False, fail_notice=False)

    result = talk.send(action='link', **dict(title='监控', text='[监控]哈哈', message_url='http://www.mootdx.com'))
    click.echo(result)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
