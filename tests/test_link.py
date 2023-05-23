import vcr


@vcr.use_cassette('tests/fixtures/vcr/test_link.yaml', match_on=['method', 'body'], record_mode='once')
def test_link(client):
    """测试发送链接消息函数"""
    result = client.link(
        title='万万没想到，某小璐竟然...',
        text='故事是这样子的...',
        message_url='http://www.kwongwah.com.my/?p=454748',
        pic_url='https://pbs.twimg.com/media/CEwj7EDWgAE5eIF.jpg'
    )

    assert (result['errcode'] == 0)
