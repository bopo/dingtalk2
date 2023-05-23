## Markdown 消息

```python
from dingtalk2 import dingtalk

access = '6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfcxxxxxxx'
secret = 'SEC0ed50da84fca5e37491b032a660dcfd2fd6aef8e2dcb74caa39ddxxxxxxxxxx'

client = dingtalk.DingTalk(access=access, secret=secret)
client.markdown(
    title='氧气文字',
    text='#### 广州天气\n'
         '> 9度，西北风1级，空气良89，相对温度73%\n\n'
         '> ![美景](http://www.sinaimg.cn/dy/slidenews/5_img/2013_28/453_28488_469248.jpg)\n'
         '> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n',
    is_at_all=True
)
```
