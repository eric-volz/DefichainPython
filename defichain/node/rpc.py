import json
import requests
import time
from defichain.logger import Logger
from defichain.node.RPCErrorHandler import RPCErrorHandler
from defichain.exceptions.http.ServiceUnavailable import ServiceUnavailable


class RPC(object):
    def __init__(self, url, logger: Logger):
        self._session = requests.Session()
        self._url = url
        self._headers = {'content-type': 'application/json'}
        self._logger = logger

    def call(self, rpc_method, *params):
        filtered_params = []
        for param in params:
            if param is not None:
                filtered_params.append(param)

        payload = json.dumps({"method": rpc_method, "params": list(filtered_params), "jsonrpc": "2.0"})
        tries = 3
        hadConnectionFailures = False

        # Logging of Node get request url
        if self._logger:
            if self._logger.log_level == "input" or self._logger.log_level == "all":
                self._logger.input("NodeInput", f"Node request URL: {self._url} | Headers: {self._headers} | Payload: {payload}")

        while True:
            try:
                response = self._session.post(self._url, headers=self._headers, data=payload)
            except requests.exceptions.ConnectionError as e:
                tries -= 1
                if tries == 0:
                    raise ServiceUnavailable(e)
                hadFailedConnections = True
                print(f"Couldn't connect for remote procedure call, will sleep for five seconds and then try again ({tries} more tries)")
                time.sleep(5)
            else:
                if hadConnectionFailures:
                    print('Connected for remote procedure call after retry.')
                break

        RPCErrorHandler(response, self._logger)  # Check for Exceptions

        result = response.json()['result']

        # Logging of Ocean get request result
        if self._logger:
            if self._logger.log_level == "output" or self._logger.log_level == "all":
                self._logger.output("NodeOutput", f"Node requests result: {result}")

        return result

    def update_url(self, url: str) -> None:
        self._url = url
