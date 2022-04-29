from .OceanException import OceanException

NOT_KEYS = ["code", "statusCode", "type"]


class OceanErrorHandler:
    def __init__(self, response):
        if "error" in response:
            args = []
            if response["error"] == "Not Found":
                keys = response.keys()
                for key in keys:
                    if not key in NOT_KEYS:
                        args.append((key, response[key]))
                raise OceanException(response["statusCode"], args)

            error = response["error"]
            httpErrorCode = error["code"]
            keys = error.keys()
            for key in keys:
                if not key in NOT_KEYS:
                    args.append((key, error[key]))

            raise OceanException(httpErrorCode, args)
