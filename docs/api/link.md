## 链接消息

```python
from dingtalk2 import dingtalk

access = '6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfcxxxxxxx'
secret = 'SEC0ed50da84fca5e37491b032a660dcfd2fd6aef8e2dcb74caa39ddxxxxxxxxxx'

client = dingtalk.DingTalk(access=access, secret=secret)

client.link(
    title='万万没想到，某小璐竟然...',
    text='故事是这样子的...',
    message_url='http://www.kwongwah.com.my/?p=454748',
    pic_url='https://pbs.twimg.com/media/CEwj7EDWgAE5eIF.jpg'
)
```
