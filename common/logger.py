import logging,os
BASEDIR = os.path.dirname(os.path.dirname(__file__))
import time

class MYLOG(logging.Logger):
    __flag=0
    def __init__(self,filename=None,level=0,type=0):
        self.logger = logging.Logger('WEB',level=level)
        fomart = logging.Formatter(fmt='%(asctime)s [%(levelname)s] %(message)s',datefmt='%Y-%m-%d %X')
        #文件日志
        sthandle = logging.FileHandler(filename=filename,encoding='utf-8')
        sthandle.setFormatter(fomart)
        #控制台日志
        cnhandle=logging.StreamHandler()
        cnhandle.setFormatter(fomart)
        if type==0:
            self.logger.addHandler(sthandle)
        elif type==1:
            self.logger.addHandler(cnhandle)
        elif type==2:
            self.logger.addHandler(sthandle)
            self.logger.addHandler(cnhandle)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg)

def logfile(filename,type=2,level='INFO'):
    time_file=os.path.join(BASEDIR,'logfile',str(time.strftime('%Y%m%d',time.localtime())))
    if not os.path.exists(time_file):
        os.mkdir(time_file)
    filename=os.path.join(time_file,filename)
    logger=MYLOG(filename=filename,level=level,type=type)
    return logger

