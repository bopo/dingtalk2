import vcr

from dingtalk2.items import ActionCard
from dingtalk2.items import CardItem


@vcr.use_cassette('tests/fixtures/vcr/test_action_card.yaml', match_on=['method', 'body'], record_mode='once')
def test_action_card(client):
    """测试发送整体跳转ActionCard消息功能（CardItem新API)"""
    btns1 = [CardItem(title='查看详情', url='https://www.dingtalk.com/')]
    actioncard1 = ActionCard(
        title='万万没想到，竟然...',
        text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
        btns=btns1,
        btn_orientation=1,
        hide_avatar=1
    )

    result = client.action(actioncard1)

    assert (result['errcode'] == 0)

    """测试发送单独跳转ActionCard消息功能"""

    btns2 = [
        CardItem(title='支持', url='https://www.dingtalk.com/'),
        CardItem(title='反对', url='http://www.back china.com/news/2018/01/11/537468.html')
    ]

    actioncard2 = ActionCard(
        title='万万没想到，竟然...',
        text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n'
             '### 故事是这样子的...',
        btns=btns2,
        btn_orientation=1,
        hide_avatar=1
    )
    result = client.action(actioncard2)

    assert (result['errcode'] == 0)


@vcr.use_cassette('tests/fixtures/vcr/test_action_card_old_api.yaml', match_on=['method', 'body'], record_mode='once')
def test_action_card_old_api(client):
    """测试发送整体跳转ActionCard消息功能（数据列表btns旧API)"""
    btns1 = [{'title': '查看详情', 'actionURL': 'https://www.dingtalk.com/'}]

    action_card1 = ActionCard(
        title='万万没想到，竟然...',
        text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
        btns=btns1,
        btn_orientation=1,
        hide_avatar=1
    )

    result = client.action(action_card1)

    assert (result['errcode'] == 0)

    """测试发送单独跳转ActionCard消息功能"""
    btns2 = [
        {'title': '支持', 'actionURL': 'https://www.dingtalk.com/'},
        {'title': '反对', 'actionURL': 'http://www.back china.com/news/2018/01/11/537468.html'}
    ]

    action_card2 = ActionCard(
        title='万万没想到，竟然...',
        text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
        btns=btns2,
        btn_orientation=1,
        hide_avatar=1
    )

    result = client.action(action_card2)

    assert (result['errcode'] == 0)
