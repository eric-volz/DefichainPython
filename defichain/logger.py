import logging
import os
import requests
from defichain.exceptions.http import WrongParameters


class Logger:
    """
    Creates a Logger object, witch can be passed to the :ref:`Node Node` and the :ref:`Ocean Ocean` object.

    There are four types of logging:

    1. input: this only logs values that are inserted into a method and errors

    2. output: this only logs values that are outputted by a method and errors

    3. error: this only logs errors.

    4. all: this logs everything

    If telegram token and telegram chatid is passed, then the logs are also sent via telegram after the respective log level.

    :param directory: (optional) directory where the logs should be stored (default: next to the script in a logs folder)
    :type directory: str
    :param log_level: (optional) input, output, error, all (default: input)
    :type log_level: str
    :param telegram_token: (optional) the telegram token
    :type telegram_token: str
    :param telegram_chatid: (optional) the telegram chatid
    :type telegram_chatid: str

    :example:

        >>> from defichain import Ocean
        >>> from defichain.logger import Logger  # import Logger
        >>>
        >>> logger = Logger(log_level="error")  # initialize logger with log level error
        >>>
        >>> ocean = Ocean(logger=logger)  # pass logger to Ocean instance
        >>>
        >>> ocean.address.getBalance("wrong_address")  # error will get logged
        Error will get logged
    """

    def __init__(self, directory: str = "logs", log_level: str = "input",
                 telegram_token: str = "", telegram_chatid: str = ""):

        if not (log_level == "input" or log_level == "output" or log_level == "error" or log_level == "all"):
            raise WrongParameters("The log level can only correspond to input, output, error or all!")

        self.directory = directory
        self.log_level = log_level
        self.telegram_token = telegram_token
        self.telegram_chatid = telegram_chatid
        self.telegram = False

        self.file = None
        self.form = None

        self.setup_logger()
        self.test_telegram()

    def setup_logger(self):
        if os.path.isdir(self.directory):
            number_of_files = len(os.listdir(self.directory))
            self.file = logging.FileHandler(filename=f"{self.directory}/defichain-python_{number_of_files + 1}.log")
        else:
            self.create_folder()
            self.file = logging.FileHandler(filename=f"{self.directory}/defichain-python_1.log")

        self.form = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s: %(message)s")
        self.file.setFormatter(self.form)

    def input(self, name, msg):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.file)

        self.telegram_send("Debug", name, msg)

        logger.debug(msg)

    def output(self, name, msg):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.file)

        self.telegram_send("Debug", name, msg)

        logger.debug(msg)

    def error(self, name, msg):
        logger = logging.getLogger(name)
        logger.setLevel(logging.ERROR)
        logger.addHandler(self.file)

        self.telegram_send("Error", name, msg)

        logger.error(msg)

    def test_telegram(self):
        if self.telegram_token != "" and self.telegram_chatid != "":
            try:
                requests.get(f"https://api.telegram.org/bot{self.telegram_token}/getUpdates")
                self.telegram = True
            except:
                print("Warning: The Telegram token for the logger is incorrect")

        if self.telegram_token != "" and self.telegram_chatid == "":
            print("Warning: You also have to submit a telegram chat id to get the logs via telegram")

        if self.telegram_token == "" and self.telegram_chatid != "":
            print("Warning: You also have to submit a telegram token to get the logs via telegram")

    def telegram_send(self, level, name, msg):
        if self.telegram:
            text = f"{level} - {name}: {msg}"
            try:
                req = requests.get(f"https://api.telegram.org/bot{self.telegram_token}/sendMessage?chat_id={self.telegram_chatid}&text={text}")
                if req.status_code != 200:
                    raise Exception("Warning: You are not using the correct telegram token and chat id combo.")
            except Exception as e:
                print(e)

    def create_folder(self):
        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)






