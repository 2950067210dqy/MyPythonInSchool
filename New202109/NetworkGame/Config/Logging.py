import json
import logging.config
import os
import logging


class loggings:
    def __init__(self,loggingConfigPath):
        self.setup_logging(default_path=loggingConfigPath)
        pass
    def setup_logging(self,default_path="logging.json",default_level=logging.INFO,env_key="LOG_CFG"):
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r") as f:
                config = json.load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
    def set_infolog(self,text=""):
        logging.info(text)
    def set_errorlog(self,text=""):
        logging.error(text)
