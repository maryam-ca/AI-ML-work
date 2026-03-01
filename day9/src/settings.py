from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = Field(..., validation_alias="APP_NAME")
    environment: str = Field(..., validation_alias="ENVIRONMENT")
    debug: bool = Field(..., validation_alias="DEBUG")

    database_url: str = Field(..., validation_alias="DATABASE_URL")
    qdrant_url: str = Field(..., validation_alias="QDRANT_URL")
    api_key: str = Field(..., validation_alias="API_KEY")


def get_settings():
    return Settings()
