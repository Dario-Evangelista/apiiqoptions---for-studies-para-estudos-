"""Module for IQ Option http verify resource."""

from apibroker.http.resource import Resource
import json

class Verify(Resource):
    """Class for IQ option verify resource."""
    # pylint: disable=too-few-public-methods

    url = ""
    def __init__(self, api, host):
        self.api = api
        if host == "ws.trade.avalonbroker.com/":
            host = 'trade.avalonbroker.com/'
        self.host = host

    def _post(self, data=None, headers=None):
        """Send get request for IQ Option API verify http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request_v2(method="POST", url=f"https://auth.{self.host}/api/v2/verify/2fa",data=json.dumps(data), headers=headers)

    def __call__(self, sms_received, token_sms):
        """Method to get IQ Option API verify http request.

        :param str sms_received: The sms received of a IQ Option server 2FA.
        :param str token_sms: The token of a IQ Option server 2FA.

        :returns: The instance of :class:`requests.Response`.
        """
        data = {"code": str(sms_received),
                "token": token_sms}

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Referer': f'https://{self.host}/en/login',
            'Sec-Fetch-Mode': 'cors',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
            }

        return self._post(data=data, headers=headers)
