from urllib.request import urlopen
from urllib.error import HTTPError


TIMEOUT = 10


class Connection:
    def __init__(self, url):
        self.url = url

    def request(self, ressource):
        """
        Requests Data from Ocean API.
        @param ressource: string Data to be requested
        @return: json
        """
        try:
            response = urlopen(self.url + ressource, timeout=TIMEOUT).read()
            return response.decode("utf-8")
        except HTTPError as e:
            raise RequestException(e.read(), e.code)


class RequestException(Exception):
    def __init__(self, message, code):
        Exception.__init__(self, message)
        self.code = code
