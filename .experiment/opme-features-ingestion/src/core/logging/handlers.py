import os
from datetime import datetime
import logging

from src.core.config import settings


class ConsoleHandler:
    
    @staticmethod
    def create(formatter: logging.Formatter, level: logging = logging.DEBUG):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        return console_handler
    

class FileHandler:
  
    @staticmethod
    def create(formatter: logging.Formatter, level: logging = logging.DEBUG):

        if not os.path.exists(settings.app.LOGS_PATH):
            os.makedirs(settings.app.LOGS_PATH)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(settings.app.LOGS_PATH, f"scraping_{timestamp}.log")
        console_handler = logging.FileHandler(log_file)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        return console_handler

