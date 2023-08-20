from datetime import datetime, timedelta


class Data:

    def __init__(self, defichainData):
        self._defichainData = defichainData

    def features(self, search: str = "", format: str = "json", filename: str = "") -> "Dict | None":
        """
        **Find available features.**

        Optionally, search for a string in the feature name or description. i.e. "tvl" to find all features related to
        total value locked.

        :param search: (optional) return only features that contain this string
        :type search: str
        :param format: (optional) return format of data (json, csv, excel) -> default: json
        :type format: str
        :param filename: (optional) provide filename to store file if not format is not json
        :type filename: str
        :return: json str -- List with possible features

            .. code-block:: json

                {
                    "endpoint": str,
                    "feature": str,
                    "description": str,
                    "earliest_entry_utc": str,
                    "latest_entry_utc": str
                }
        """
        return self._defichainData._conn.get("features", {"search": search, "format": format, "filename": filename})

    def history(self,
                features: "str | List",
                interval: str = "daily",
                columns: str = "avg",
                to_timestamp: str = datetime.utcnow(),
                from_timestamp: str = datetime.utcnow() - timedelta(days=90),
                format: str = "json",
                filename: str = ""):
        return self._defichainData._conn.get("history", {"features": features,
                                                         "interval": interval,
                                                         "columns": columns,
                                                         "to_timestamp": to_timestamp,
                                                         "from_timestamp": from_timestamp,
                                                         "format": format,
                                                         "filename": filename})

    def value(self, feature: str, interval: str = "daily", timestamp: str = datetime.utcnow()):
        return self._defichainData._conn.get("value", {"feature": feature,
                                                       "interval": interval,
                                                       "timestamp": timestamp,
                                                       })

