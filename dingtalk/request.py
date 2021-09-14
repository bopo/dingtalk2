import httpx
from loguru import logger


class Request:
    def __init__(self, webhook, headers, options):
        self.webhook = webhook
        self.headers = headers
        self.options = options
        self.session = httpx.Client()

    def get(self, payloads=None):
        return self.request(method='GET', data=payloads)

    def post(self, payloads):
        return self.request(method='POST', data=payloads)

    @logger.catch()
    def request(self, method='GET', data: dict = None):

        logger.warning(self.webhook)

        try:
            response = self.session.request(method=method, url=self.webhook, headers=self.headers, json=data, params=self.options)
            response.raise_for_status()
            logger.warning(response.json())
            return response.json()
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
            logger.error("消息发送失败， HTTP error: %d, reason: %s" % (exc.response.status_code, exc))
            return exc.response.json()
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
            return None
        except httpx.ConnectError as exc:
            logger.error("消息发送失败，HTTP connection error!")
            return None
        except httpx.Timeout:
            logger.error("消息发送失败，Timeout error!")
            return None

    @staticmethod
    def _success(response):
        return response.json()
