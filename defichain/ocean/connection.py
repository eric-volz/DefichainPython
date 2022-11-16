import requests
import json
from defichain.logger import Logger
from defichain.ocean.OceanErrorHandler import OceanErrorHandler


class Connection:
    def __init__(self, url, logger: Logger):
        self._url = url
        self._session = requests.Session()
        self._headers = {'content-type': 'application/json'}
        self._logger = logger

    def get(self, data, size=None, next=None):
        url = self._url + data
        if size is not None and next is not None:
            url += f"?size={size}&next={next}"
        elif size is not None:
            url += f"?size={size}"
        elif next is not None:
            url += f"?next={next}"

        # Logging of Ocean get request url
        if self._logger:
            if self._logger.log_level == "input" or self._logger.log_level == "all":
                self._logger.input("OceanInput", f"Get request url: {url}")

        response = requests.get(url)
        OceanErrorHandler(response, self._logger)  # Handle Exceptions

        result = json.loads(response.text)

        # Logging of Ocean get request result
        if self._logger:
            if self._logger.log_level == "output" or self._logger.log_level == "all":
                self._logger.output("OceanOutput", f"Result of get request: {result}")

        return result

    def post(self, method, params):
        if method == "rawtx/send" or method == "rawtx/test":
            payload = params
        else:
            payload = json.dumps({"params": list(params), "jsonrpc": "2.0"})

        # Logging of Ocean post request
        if self._logger:
            if self._logger.log_level == "input" or self._logger.log_level == "all":
                self._logger.input("OceanInput", f"Post request: {self._url + method, self._headers, payload}")

        response = self._session.post(self._url + method, headers=self._headers, data=payload)
        OceanErrorHandler(response, self._logger)  # Handle Exceptions

        result = response.json()

        # Logging of Ocean get requests result
        if self._logger:
            if self._logger.log_level == "output" or self._logger.log_level == "all":
                self._logger.output("OceanOutput", f"Result of post request: {result}")

        return result
