import pytest as pytest

from dingtalk2.dingtalk import DingTalk


@pytest.fixture(scope='session')
def client():
    access = '6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfc5ed89'
    secret = 'SEC0ed50da84fca5e37491b032a660dcfd2fd6aef8e2dcb74caa39ddb434421ad78'
    return DingTalk(access=access, secret=secret)
