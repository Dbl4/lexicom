from enum import Enum
from logging import config as logging_config

from core.logger import LOGGING
from pydantic import BaseSettings, Field, RedisDsn

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)


class LoggerLevel(str, Enum):
    critical = "CRITICAL"
    error = "ERROR"
    warning = "WARNING"
    info = "INFO"
    debug = "DEBUG"
    notset = "NOTSET"


class Settings(BaseSettings):
    logger_level: LoggerLevel = LoggerLevel.debug
    project_name: str = Field(
        "Lexicom-project",
        env="PROJECT_NAME",
    )
    host: str = Field("0.0.0.0", env="HOST")
    port: int = Field(8000, env="PORT")
    redis_dsn: RedisDsn = Field("redis://localhost:6379", env="REDIS_DSN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
