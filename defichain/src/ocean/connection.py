import requests
import json
from .exceptions.OceanErrorHandler import OceanErrorHandler


class Connection:
    def __init__(self, url):
        self._url = url
        self._session = requests.Session()
        self._headers = {'content-type': 'application/json'}

    def get(self, data, size=None, next=None):
        url = self._url + data
        if size is not None and next is not None:
            url += f"?size={size}&next={next}"
        elif size is not None:
            url += f"?size={size}"
        elif next is not None:
            url += f"?next={next}"
        result = json.loads(requests.get(url).text)
        OceanErrorHandler(result)  # Handle Exceptions
        return result

    def post(self, method, params):
        payload = json.dumps({"params": list(params), "jsonrpc": "2.0"})
        response = self._session.post(self._url + method, headers=self._headers, data=payload)
        result = response.json()
        OceanErrorHandler(result)  # Handle Exceptions
        return result
