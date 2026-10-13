"""Application settings, loaded from environment / .env."""
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Dashboards (Render, Vercel) sometimes capture a trailing newline or stray
    # space when a value is pasted into an env var. A newline in a URL or an HTTP
    # header value makes the outgoing request malformed and raises at call time
    # (this has broken DATABASE_URL and SUPABASE_ANON_KEY here before). Strip
    # surrounding whitespace from every string setting so it can't recur.
    @field_validator("*", mode="before")
    @classmethod
    def _strip_whitespace(cls, v):
        return v.strip() if isinstance(v, str) else v

    cohere_api_key: str
    database_url: str = ""
    redis_url: str = ""
    supabase_url: str = ""
    supabase_anon_key: str = ""
    allowed_origins: str = "http://localhost:3000"

    embed_model: str = "embed-multilingual-v3.0"
    embed_dim: int = 1024
    rerank_model: str = "rerank-multilingual-v3.0"
    chat_model: str = "command-r-08-2024"

    chunk_size: int = 450
    chunk_overlap: int = 90

    db_path: str = "data/docuchat.db"


settings = Settings()
