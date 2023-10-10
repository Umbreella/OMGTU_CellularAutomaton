from pydantic_settings import BaseSettings


class Config(BaseSettings):
    WIDTH: int = 600
    HEIGHT: int = 600
    PIXELS_IN_POINT: int = 6

    class Config:
        env_prefix = 'APP_APPLICATION_'


config = Config()
