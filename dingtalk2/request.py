import requests

from .logger import logger


class Request:
    def __init__(self, webhook, headers, options):
        self.webhook = webhook
        self.headers = headers
        self.options = options
        self.session = requests.Session()

    def get(self, payloads=None):
        return self.request(method='GET', data=payloads)

    def post(self, payloads):
        return self.request(method='POST', data=payloads)

    def request(self, method='GET', data: dict = None):
        logger.debug(self.webhook)

        try:
            response = self.session.request(method=method, url=self.webhook, headers=self.headers, json=data, params=self.options)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as exc:
            logger.warning(f'Error response {exc.response.status_code} while requesting {exc.request.url!r}.')
            logger.error(f'消息发送失败， HTTP error: {exc.response.status_code:d}, reason: {exc}')
            logger.exception(exc)
            return exc.response.json()
        except requests.exceptions.ConnectTimeout:
            logger.error('消息发送失败，Timeout error!')
            return None
        except requests.exceptions.ConnectionError as exc:
            logger.exception(exc)
            logger.error('消息发送失败，HTTP connection error!')
            return None
        except requests.exceptions.RequestException as exc:
            logger.warning(f'An error occurred while requesting {exc.request.url!r}.')
            return None

    @staticmethod
    def _success(response):
        return response.json()
