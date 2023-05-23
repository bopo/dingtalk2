import vcr


@vcr.use_cassette('tests/fixtures/vcr/test_text.yaml', match_on=['method', 'body'], record_mode='once')
def test_text(client):
    """测试发送文本消息函数"""
    result = client.text(msg='我就是小丁，小丁就是我！', at_all=True)
    assert result['errcode'] == 0, result
