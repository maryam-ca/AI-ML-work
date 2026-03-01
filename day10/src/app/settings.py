from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str


def get_settings():
    return Settings()
