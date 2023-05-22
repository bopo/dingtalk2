from .logger import logger
from .utils import is_not_null_and_blank_str


class ActionCard:
    """
    ActionCard类型消息格式（整体跳转、独立跳转）
    """

    def __init__(self, title, text, btns, btn_orientation=0, hide_avatar=0):
        """
        ActionCard初始化
        :param title: 首屏会话透出的展示内容
        :param text: markdown格式的消息
        :param btns: 按钮列表：（1）按钮数量为1时，整体跳转ActionCard类型；（2）按钮数量大于1时，独立跳转ActionCard类型；
        :param btn_orientation: 0：按钮竖直排列，1：按钮横向排列（可选）
        :param hide_avatar: 0：正常发消息者头像，1：隐藏发消息者头像（可选）
        """
        self.title = title
        self.text = text
        self.btn_orientation = btn_orientation
        self.hide_avatar = hide_avatar

        btn_list = [btn.get_data() for btn in btns if isinstance(btn, CardItem)]

        # 兼容：1、传入CardItem示例列表；2、传入数据字典列表
        self.btns = btn_list if btn_list else btns

    def get_data(self):
        """
        获取ActionCard类型消息数据（字典）
        :return: 返回ActionCard数据
        """
        if all(map(is_not_null_and_blank_str, [self.title, self.text])) and len(self.btns):
            if len(self.btns) == 1:
                # 整体跳转ActionCard类型
                data = {
                    'msgtype': 'actionCard',
                    'actionCard': {
                        'title': self.title,
                        'text': self.text,
                        'hideAvatar': self.hide_avatar,
                        'btnOrientation': self.btn_orientation,
                        'singleTitle': self.btns[0]['title'],
                        'singleURL': self.btns[0]['actionURL']
                    }
                }
                return data
            else:
                # 独立跳转ActionCard类型
                data = {
                    'msgtype': 'actionCard',
                    'actionCard': {
                        'title': self.title,
                        'text': self.text,
                        'hideAvatar': self.hide_avatar,
                        'btnOrientation': self.btn_orientation,
                        'btns': self.btns
                    }
                }
                return data

        logger.error('ActionCard类型，消息标题或内容或按钮数量不能为空！')
        raise ValueError('ActionCard类型，消息标题或内容或按钮数量不能为空！')


class FeedLink:
    """
    FeedCard类型单条消息格式
    """

    def __init__(self, title, message_url, pic_url):
        """
        初始化单条消息文本
        :param title: 单条消息文本
        :param message_url: 点击单条信息后触发的URL
        :param pic_url: 点击单条消息后面图片触发的URL
        """
        super().__init__()
        self.title = title
        self.message_url = message_url
        self.pic_url = pic_url

    def get_data(self):
        """
        获取FeedLink消息数据（字典）
        :return: 本FeedLink消息的数据
        """
        if all(map(is_not_null_and_blank_str, [self.title, self.message_url, self.pic_url])):
            data = {
                'title': self.title,
                'messageURL': self.message_url,
                'picURL': self.pic_url
            }
            return data

        logger.error('FeedCard类型单条消息文本、消息链接、图片链接不能为空！')
        raise ValueError('FeedCard类型单条消息文本、消息链接、图片链接不能为空！')


class CardItem:
    """
    ActionCard和FeedCard消息类型中的子控件

    注意：
    1、发送FeedCard消息时，参数pic_url必须传入参数值；
    2、发送ActionCard消息时，参数pic_url不需要传入参数值；
    """

    def __init__(self, title, url, pic_url=None):
        """
        CardItem初始化
        @param title: 子控件名称
        @param url: 点击子控件时触发的URL
        @param pic_url: FeedCard的图片地址，ActionCard时不需要，故默认为None
        """
        self.url = url
        self.title = title
        self.pic_url = pic_url

    def get_data(self):
        """
        获取CardItem子控件数据（字典）
        @return: 子控件的数据
        """
        if all(map(is_not_null_and_blank_str, [self.title, self.url, self.pic_url])):
            # FeedCard类型
            data = {
                'title': self.title,
                'picURL': self.pic_url,
                'messageURL': self.url,
            }

            return data
        elif all(map(is_not_null_and_blank_str, [self.title, self.url])):
            # ActionCard类型
            data = {
                'title': self.title,
                'actionURL': self.url,
            }

            return data

        logger.error('CardItem是ActionCard的子控件时，title、url不能为空；是FeedCard的子控件时，title、url、pic_url不能为空！')
        raise ValueError('CardItem是ActionCard的子控件时，title、url不能为空；是FeedCard的子控件时，title、url、pic_url不能为空！')


__all__ = ('ActionCard', 'FeedLink', 'CardItem')
