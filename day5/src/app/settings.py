from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    app_name: str = Field(default="FastAPI App", validation_alias="APP_NAME")
    environment: str = Field(default="dev", validation_alias="ENVIRONMENT")
    debug: bool = Field(default=False, validation_alias="DEBUG")
    host: str = Field(default="127.0.0.1", validation_alias="HOST")
    port: int = Field(default=8000, validation_alias="PORT")
    api_key: str = Field(..., validation_alias="API_KEY")
    allowed_origins_raw: str = Field(default="", validation_alias="ALLOWED_ORIGINS")

    @property
    def allowed_origins(self) -> List[str]:
        return [x.strip() for x in self.allowed_origins_raw.split(",") if x.strip()]


@lru_cache
def get_settings():
    return Settings()
