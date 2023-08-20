import requests
from typing import Dict


class Connection:

    def __init__(self, url: str):
        self.url = url

    def get(self, function: str, params: Dict, filename: str = None):
        """
        Retrieves information from the API
        Packs the provided data to the correct format.

        :param function: (required) API function to use
        :type function: str
        :param params: (required) parameters to insert
        :type params: Dict
        :param filename: (optional) filename to store file if not format is not json
        :type filename: str
        :return: str | None - returns information as json or stores information in a file
        """
        parameter_list = []
        for key in params.keys():
            if isinstance(params[key], list):
                for feature in params[key]:
                    parameter_list.append(f"{key}={feature}")
            else:
                parameter_list.append(f"{key}={params[key]}")
        parameter_str = "&".join(parameter_list).replace(":", "%3A")

        url = f"{self.url}{function}?{parameter_str}"

        response = requests.get(url)

        if params.get("format") in ("json", None):
            return response.json()
        else:
            if not filename and params.get("format"):
                raise AttributeError("You need to provide a filename to store the received data.")

            if params.get("format") == "csv":
                with open(filename, "w") as f:
                    f.write(response.text)
            elif params.get("format") == "excel":
                pass


if __name__ == "__main__":
    conn = Connection("https://api.defichain-data.com/")

    print(conn.get("features", {"search": "", "format": "csv"}, "test.csv"))

