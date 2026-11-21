"""Environment settings."""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    qtl_root: str | None = None
    fred_api_key: str | None = None
    hf_token: str | None = None


def get_settings() -> Settings:
    return Settings()
