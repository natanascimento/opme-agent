import logging

from dataclasses import dataclass

from src.core.config import settings


@dataclass
class LoggerConfig:
    name: str = "scraping-logger"
    formatt: str = (
        "[%(asctime)s] {{%(funcName)s:%(lineno)d}} %(levelname)s - %(message)s"
    )
    level: logging = logging.DEBUG

    def __post_init__(self):
        if settings.app.ENV == "prod":
            self.level = logging.WARN

