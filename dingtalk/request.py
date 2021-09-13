import httpx
from loguru import logger


class Request:
    def __init__(self, webhook, headers, options):
        self.webhook = webhook
        self.headers = headers
        self.options = options
        self.session = httpx.Client()

    def get(self, payloads=None):
        self.request(method='GET', data=payloads)

    def post(self, payloads):
        self.request(method='POST', data=payloads)

    def request(self, method='GET', data: dict = None):
        try:
            response = self.session.request(method=method, url=self.webhook, headers=self.headers, json=data, params=self.options)
            response.raise_for_status()
            return self._success(response)
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
            logger.error("消息发送失败， HTTP error: %d, reason: %s" % (exc.response.status_code, exc))
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
        except httpx.ConnectError as exc:
            logger.error("消息发送失败，HTTP connection error!")
            raise
        except httpx.Timeout:
            logger.error("消息发送失败，Timeout error!")
            raise

    @staticmethod
    def _success(response):
        return response.json()
