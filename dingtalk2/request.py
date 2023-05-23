import httpx

from .logger import logger


class Request:
    def __init__(self, webhook, headers, options):
        self.webhook = webhook
        self.headers = headers
        self.options = options
        self.session = httpx.Client(verify=False)

    def get(self, payloads=None):
        return self.request(method='GET', data=payloads)

    def post(self, payloads):
        return self.request(method='POST', data=payloads)

    def request(self, method='GET', data: dict = None):
        try:
            payloads = dict(method=method, url=self.webhook, headers=self.headers, json=data, params=self.options)
            response = self.session.request(**payloads)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            logger.warning(f'Error response {exc.response.status_code} while requesting {exc.request.url!r}.')
            logger.error(f'消息发送失败， HTTP error: {exc.response.status_code:d}, reason: {exc}')
            logger.exception(exc)
            return exc.response.json()
        except httpx.ConnectTimeout:
            logger.error('消息发送失败，Timeout error!')
            return None
        except httpx.ConnectError as exc:
            logger.exception(exc)
            logger.error('消息发送失败，HTTP connection error!')
            return None
        except httpx.RequestError as exc:
            logger.warning(f'An error occurred while requesting {exc.request.url!r}.')
            return None

    @staticmethod
    def _success(response):
        return response.json()
