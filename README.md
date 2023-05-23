# DingTalk2 介绍

[![image](https://img.shields.io/pypi/v/dingtalk2.svg)](https://pypi.python.org/pypi/dingtalk2)
[![image](https://img.shields.io/travis/bopo/dingtalk2.svg)](https://travis-ci.com/bopo/dingtalk2)
[![Documentation Status](https://readthedocs.org/projects/dingtalk2/badge/?version=latest)](https://dingtalk2.readthedocs.io/en/latest/?version=latest)

钉钉支持 Webhook 模式接入事件推送、机器人收消息以及卡片回调等

-   开源协议: MIT license
-   使用文档: <https://dingtalk2.readthedocs.io>.

## 快速开始

### 准备工作

* Python3 开发环境，https://www.python.org/
* 钉钉机器人的 token

### 快速开始指南

1、安装 dingtalk2

```Shell
python -m pip install dingtalk2
```

2、使用 dingtalk2

```python
from dingtalk2 import dingtalk

access = '6eab6a1161ea33c2693aae53fe92c298469f685aed8261ffdfd15d2bcfcxxxxxxx'
secret = 'SEC0ed50da84fca5e37491b032a660dcfd2fd6aef8e2dcb74caa39ddxxxxxxxxxx'

client = dingtalk.DingTalk(access=access, secret=secret)

client.text("hello")
client.image(pic_url='http://uc-test-manage-00.umlife.net/jenkins/pic/flake8.png')

```


### 技术支持

可以搜索共创群，答疑交流。

共创群ID：xxx （钉钉搜索群号入群）；

也可以扫码入群：

