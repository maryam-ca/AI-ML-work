from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    qdrant_url: str

    class Config:
        env_file = ".env.compose"


settings = Settings()
