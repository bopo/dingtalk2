## 卡片消息

```python
from dingtalk2 import dingtalk
from dingtalk2.items import CardItem, ActionCard

access = '6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfcxxxxxxx'
secret = 'SEC0ed50da84fca5e37491b032a660dcfd2fd6aef8e2dcb74caa39ddxxxxxxxxxx'

client = dingtalk.DingTalk(access=access, secret=secret)

# 测试发送整体跳转ActionCard消息功能（CardItem新API)
result = client.action(ActionCard(
    title='万万没想到，竟然...',
    text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n### 故事是这样子的...',
    btns=[CardItem(title='查看详情', url='https://www.dingtalk.com/')],
    btn_orientation=1,
    hide_avatar=1
))

# """测试发送单独跳转ActionCard消息功能"""

client.action(ActionCard(
    title='万万没想到，竟然...',
    text='![markdown](http://www.songshan.es/wp-content/uploads/2016/01/Yin-Yang.png) \n'
         '### 故事是这样子的...',
    btns=[
        CardItem(title='支持', url='https://www.dingtalk.com/'),
        CardItem(title='反对', url='http://www.back china.com/news/2018/01/11/537468.html')
    ],
    btn_orientation=1,
    hide_avatar=1
))
```
