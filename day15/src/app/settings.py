from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")

    qdrant_url: str = Field(default="http://127.0.0.1:6333")
    qdrant_collection_name: str = Field(default="week2_day13_chunks")
    default_search_limit: int = Field(default=3)

    embedding_model_name: str = Field(
        default="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    groq_api_key: str = Field(..., alias="GROQ_API_KEY")
    groq_model_name: str = Field(default="llama-3.1-8b-instant", alias="GROQ_MODEL")


settings = Settings()
