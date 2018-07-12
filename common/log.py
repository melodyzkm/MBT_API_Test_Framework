import logging
import threading
import os
from datetime import datetime
import get_config

class Log:
    def __init__(self):
        global logPath, resultPath, cwd_dir_path
        cwd_dir_path = get_config.cwd_dir_path
        resultPath = os.path.join(cwd_dir_path, "result")
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        log_path = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d_%H%M%S")))
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        # set logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # set file handler
        file_handler  = logging.FileHandler(os.path.join(log_path, "output.log"))
        # set formatter
        formatter = logging.Formatter("%(asctime)s %(filename)s: %(levelname)s %(message)s")
        file_handler.setFormatter(formatter)

        # set stream handler
        console = logging.StreamHandler()
        console.setFormatter(formatter)

        # add handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console)

    def get_logger(self):
        return self.logger


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log


