## 卡片消息

```python
from dingtalk2 import dingtalk
from dingtalk2.items import FeedLink

access = '6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfcxxxxxxx'
secret = 'SEC0ed50da84fca5e37491b032a660dcfd2fd6aef8e2dcb74caa39ddxxxxxxxxxx'

client = dingtalk.DingTalk(access=access, secret=secret)

result = client.feed([
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
])
```
