import vcr

from dingtalk2.items import CardItem
from dingtalk2.items import FeedLink


@vcr.use_cassette('tests/fixtures/vcr/test_feed_card.yaml', match_on=['method', 'body'], record_mode='once')
def test_feed_card(client):
    """测试发送FeedCard类型消息功能（CardItem新API)"""
    cards = [
        CardItem(
            title="氧气美女", url="https://www.dingtalk.com/",
            pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg"
        ),
        CardItem(
            title="氧眼美女", url="https://www.dingtalk.com/",
            pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg"
        ),
        CardItem(
            title="氧神美女", url="https://www.dingtalk.com/",
            pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg"
        )
    ]

    result = client.feed(cards)

    assert result['errcode'] == 0, result


@vcr.use_cassette('tests/fixtures/vcr/test_feed_link.yaml', match_on=['method', 'body'], record_mode='once')
def test_feed_link(client):
    """测试发送FeedCard类型消息功能(FeedLink旧API)"""
    links = [
        FeedLink(
            title="氧气美女", message_url="https://www.dingtalk.com/",
            pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg"
        ),
        FeedLink(
            title="氧眼美女", message_url="https://www.dingtalk.com/",
            pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg"
        ),
        FeedLink(
            title="氧神美女", message_url="https://www.dingtalk.com/",
            pic_url="http://pic1.win4000.com/wallpaper/2020-03-11/5e68b0557f3a6.jpg"
        )
    ]

    result = client.feed(links)

    assert result['errcode'] == 0, result
