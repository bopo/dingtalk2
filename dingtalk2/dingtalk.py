import base64
import hashlib
import hmac
import queue
import re
import time
from urllib.parse import quote_plus

from .constants import HEADERS, GATEWAY
from .items import ActionCard
from .items import CardItem
from .items import FeedLink
from .logger import logger
from .request import Request
from .utils import is_not_null_and_blank_str


class DingTalk:
    """
    钉钉群自定义机器人（每个机器人每分钟最多发送20条），支持文本（text）、连接（link）、markdown三种消息类型！
    """

    # gateway = 'https://oapi.dingtalk.com/robot/send'
    # headers = {'Content-Type': 'application/json; charset=utf-8'}
    # options = {}
    # webhook = ''
    session: Request

    def __init__(self, access: str = None, secret: str = None, pc_slide=False, fail_notice=False):
        """
        机器人初始化
        :param access: 钉钉群自定义机器人webhook地址
        :param secret: 机器人安全设置页面勾选“加签”时需要传入的密钥
        :param pc_slide: 消息链接打开方式，默认False为浏览器打开，设置为True时为PC端侧边栏打开
        :param fail_notice: 消息发送失败提醒，默认为False不提醒，开发者可以根据返回的消息发送结果自行判断和处理
        """

        self.queue = queue.Queue(20)  # 钉钉官方限流每分钟发送20条信息
        self.secret = secret

        # self.webhook = f"https://oapi.dingtalk.com/robot/send?access_token={access}"
        self.options = {'access_token': access}

        self.fail_notice = fail_notice
        self.start_time = time.time()
        self.pc_slide = pc_slide

        # 初始化参数
        self._signature()

    def _signature(self):
        """ 钉钉群自定义机器人安全设置加签时，签名中的时间戳与请求时不能超过一个小时，所以每个1小时需要更新签名 """
        if self.secret and self.secret.startswith('SEC'):
            timestamp = round(self.start_time * 1000)
            string_to_sign = f'{timestamp}\n{self.secret}'

            code = hmac.new(self.secret.encode(), string_to_sign.encode(), digestmod=hashlib.sha256).digest()
            sign = quote_plus(base64.b64encode(code))

            self.options.update({'timestamp': timestamp, 'sign': sign})

        self.session = Request(webhook=GATEWAY, headers=HEADERS, options=self.options)

    def _open_type(self, url):
        """ 消息链接的打开方式
        1、默认或不设置时，为浏览器打开：pc_slide=False
        2、在PC端侧边栏打开：pc_slide=True
        """
        slide = ('false', 'true')[bool(self.pc_slide)]

        return f'dingtalk://dingtalkclient/page/link?url={quote_plus(url)}&pc_slide={slide}'

    def text(self, msg, at_all=False, at: list = None, at_ids: list = None, auto_at=True):
        """ text类型
        :type at_ids: object
        :param msg: 消息内容
        :param at_all: @所有人时：true，否则为false（可选）
        :param at: 被@人的手机号（注意：可以在msg内容里自定义@手机号的位置，也支持同时@多个手机号，可选）
        :param at_ids: 被@人的dingtalkId（可选）
        :param auto_at: 是否自动在msg内容末尾添加@手机号，默认自动添加，可设置为False取消（可选）
        :return: 返回消息发送结果
        """
        payload = {'msgtype': 'text', 'at': {}}

        if not is_not_null_and_blank_str(msg):
            raise ValueError('text类型，消息内容不能为空！')

        payload['text'] = {'content': msg}

        if at_all:
            payload['at']['isAtAll'] = at_all

        if at:
            at = list(map(str, at))
            payload['at']['atMobiles'] = at

            if auto_at:
                mobiles_text = '\n@' + '@'.join(at)
                payload['text']['content'] = msg + mobiles_text

        if at_ids:
            at_ids = list(map(str, at_ids))
            payload['at']['atDingtalkIds'] = at_ids

        logger.debug(f'text类型：{payload}')

        return self._request(payload)

    def image(self, pic_url):
        """ image类型（表情）
        :param pic_url: 图片链接
        :return: 返回消息发送结果
        """
        if is_not_null_and_blank_str(pic_url):
            data = {'msgtype': 'image', 'image': {'picURL': pic_url}}
            logger.debug(f'image类型：{data}')
            return self._request(data)

        raise ValueError('image类型中图片链接不能为空！')

    def link(self, title, text, message_url, pic_url=''):
        """ link类型
        :param title: 消息标题
        :param text: 消息内容（如果太长自动省略显示）
        :param message_url: 点击消息触发的URL
        :param pic_url: 图片URL（可选）
        :return: 返回消息发送结果

        """
        if all(map(is_not_null_and_blank_str, [title, text, message_url])):
            payload = {
                'msgtype': 'link',
                'link': {
                    'text': text,
                    'title': title,
                    'picUrl': pic_url,
                    'messageUrl': self._open_type(message_url)
                }
            }

            logger.debug(f'link类型：{payload}')
            return self._request(payload)

        raise ValueError('link类型中消息标题或内容或链接不能为空！')

    def markdown(self, title, text, is_at_all=False, at_mobiles=None, at_dingtalk_ids=None, is_auto_at=True):
        """ markdown类型
        :param title: 首屏会话透出的展示内容
        :param text: markdown格式的消息内容
        :param is_at_all: @所有人时：true，否则为：false（可选）
        :param at_mobiles: 被@人的手机号（默认自动添加在text内容末尾，可取消自动化添加改为自定义设置，可选）
        :param at_dingtalk_ids: 被@人的dingtalkId（可选）
        :param is_auto_at: 是否自动在text内容末尾添加@手机号，默认自动添加，可设置为False取消（可选）
        :return: 返回消息发送结果
        """
        if at_mobiles is None:
            at_mobiles = []

        if at_dingtalk_ids is None:
            at_dingtalk_ids = []

        if all(map(is_not_null_and_blank_str, [title, text])):
            # 给 Markdown 文本消息中的跳转链接添加上跳转方式
            func = lambda m: m.group(0).replace(m.group(1), self._open_type(m.group(1)))  # noqa
            text = re.sub(r'(?<!!)\[.*?\]\((.*?)\)', func, text)  # noqa

            payload = {'msgtype': 'markdown', 'markdown': {'title': title, 'text': text}, 'at': {}}

            if is_at_all:
                payload['at']['isAtAll'] = is_at_all

            if at_mobiles:
                at_mobiles = list(map(str, at_mobiles))
                payload['at']['atMobiles'] = at_mobiles

                if is_auto_at:
                    mobiles_text = '\n@' + '@'.join(at_mobiles)
                    payload['markdown']['text'] = text + mobiles_text

            if at_dingtalk_ids:
                at_dingtalk_ids = list(map(str, at_dingtalk_ids))
                payload['at']['atDingtalkIds'] = at_dingtalk_ids

            logger.debug(f'markdown类型：{payload}')
            return self._request(payload)

        raise ValueError('markdown类型中消息标题或内容不能为空！')

    def action(self, action_card):
        """ ActionCard类型
        :param action_card: 整体跳转ActionCard类型实例或独立跳转ActionCard类型实例
        :return: 返回消息发送结果
        """
        if isinstance(action_card, ActionCard):
            payload = action_card.get_data()

            if 'singleURL' in payload['actionCard']:
                payload['actionCard']['singleURL'] = self._open_type(payload['actionCard']['singleURL'])

            if 'btns' in payload['actionCard']:
                for btn in payload['actionCard']['btns']:
                    btn['actionURL'] = self._open_type(btn['actionURL'])

            logger.debug('ActionCard类型：%s' % payload)
            return self._request(payload)

        raise TypeError(f'ActionCard类型：传入的实例类型不正确，内容为：{str(action_card)}')

    def feed(self, links):
        """ FeedCard类型
        :param links: FeedLink实例列表 or CardItem实例列表
        :return: 返回消息发送结果
        """
        if not isinstance(links, list):
            logger.error(f'FeedLink类型：传入的数据格式不正确，内容为：{str(links)}')
            raise ValueError(f'FeedLink类型：传入的数据格式不正确，内容为：{str(links)}')

        link_list = []

        for link in links:
            if not isinstance(link, FeedLink) and not isinstance(link, CardItem):
                raise ValueError(f'FeedLink类型，传入的数据格式不正确，内容为：{str(link)}')

            # 兼容：1、传入FeedLink实例列表；2、CardItem实例列表；
            link = link.get_data()
            link['messageURL'] = self._open_type(link['messageURL'])
            link_list.append(link)

        payload = {'msgtype': 'feedCard', 'feedCard': {'links': link_list}}
        logger.debug(f'FeedCard类型：{payload}')

        return self._request(payload)

    def _request(self, payload: dict) -> dict:
        """ 发送消息（内容UTF-8编码）
        :param payload: 消息数据（字典）
        :return: 返回消息发送结果
        """
        now = time.time()

        # 钉钉自定义机器人安全设置加签时，签名中的时间戳与请求时不能超过一个小时，所以每个1小时需要更新签名
        if now - self.start_time >= 3600 and self.secret and self.secret.startswith('SEC'):
            self.start_time = now
            self._signature()

        # 钉钉自定义机器人现在每分钟最多发送20条消息
        self.queue.put(now)

        if self.queue.full():
            elapse_time = now - self.queue.get()
            if elapse_time < 60:
                sleep_time = int(60 - elapse_time) + 1
                logger.debug(f'钉钉官方限制机器人每分钟最多发送20条，当前发送频率已达限制条件，休眠 {str(sleep_time)}s')
                time.sleep(sleep_time)

        return self.session.post(payload)

    def send(self, action='text', **kwargs):
        """
        发送消息

        :param action:
        :param kwargs:
        :return:
        """
        return getattr(self, action)(**kwargs)
