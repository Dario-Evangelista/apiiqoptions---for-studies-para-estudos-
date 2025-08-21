"""Module for IQ Option http login resource."""

from apibroker.http.resource import Resource

class Events(Resource):
    """Class for IQ option login resource."""
    # pylint: disable=too-few-public-methods

    url = ""
    def __init__(self, api, host):
        self.api = api
        self.host = host

    def send_http(self,method, data=None, headers=None):
        """Send get request for IQ Option API login http resource.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request_v2(method=method, url=f"https://event.{self.host}/api/v1/events",data=data)

    def __call__(self,method,data, headers=None):
        """Method to get IQ Option API login http request.

        :param str username: The username of a IQ Option server.
        :param str password: The password of a IQ Option server.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_http(method=method,data=data,headers=headers)
