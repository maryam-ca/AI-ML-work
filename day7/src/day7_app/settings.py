from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    api_key: str

    model_config = ConfigDict(env_file=".env")


settings = Settings()
