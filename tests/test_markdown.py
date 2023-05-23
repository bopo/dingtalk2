import vcr


@vcr.use_cassette('tests/fixtures/vcr/test_markdown.yaml', match_on=['method', 'body'], record_mode='once')
def test_markdown(client):
    """测试发送Markdown格式消息函数"""
    result = client.markdown(
        title='氧气文字',
        text='#### 广州天气\n'
             '> 9度，西北风1级，空气良89，相对温度73%\n\n'
             '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
             '> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n',
        is_at_all=True
    )
    assert (result['errcode'] == 0)
