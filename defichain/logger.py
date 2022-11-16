import logging
import os


class Logger:

    def __init__(self):
        if os.path.isdir("logs"):
            number_of_files = len(os.listdir("logs"))
            self.file = logging.FileHandler(filename=f"logs/defichain-python_{number_of_files + 1}.log")
        else:
            self.create_folder()
            self.file = logging.FileHandler(filename="logs/defichain-python_1.log")

        self.form = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s: %(message)s")
        self.file.setFormatter(self.form)

    def get_debug_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.file)
        return logger

    def get_error_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.ERROR)
        logger.addHandler(self.file)
        return logger

    def get_result_logger(self, name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(self.file)
        return logger

    @staticmethod
    def create_folder():
        if not os.path.isdir("logs"):
            os.mkdir("logs")






