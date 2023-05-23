import vcr


@vcr.use_cassette('tests/fixtures/vcr/test_image.yaml', match_on=['method', 'body'], record_mode='once')
def test_image(client):
    """测试发送表情图片消息函数"""
    result = client.image(pic_url='http://uc-test-manage-00.umlife.net/jenkins/pic/flake8.png')
    assert (result['errcode'] == 0)
