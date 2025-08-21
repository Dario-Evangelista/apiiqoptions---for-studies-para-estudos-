"""Module for IQ Option http login resource."""

from apibroker.http.resource import Resource


class Logout(Resource):
    """Class for IQ option login resource."""
    # pylint: disable=too-few-public-methods

    url = ""
    def __init__(self, api, host):
        self.api = api
        if host == "ws.trade.avalonbroker.com/":
            host = 'trade.avalonbroker.com/'
        self.host = host

    def _post(self, data=None, headers=None):
        """Send get request for IQ Option API login http resource.

        :returns: The instance of :class:`requests.Response`.
        
        """
        if self.host == 'trade.avalonbroker.com/':
            v2 = 'v2'
        else:
            v2 = 'v2'
        return self.api.send_http_request_v2(method="POST", url=f"https://auth.{self.host}/api/v1.0/logout",data=data, headers=headers)

    def __call__(self):
       
        return self._post()

