from functools import lru_cache
from typing import List, Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	cors_allow_origins: List[str] = ["http://localhost:5173", "http://localhost:3000", "*"]
	default_language: str = "en"
	default_location: str = "US"
	default_tone: str = "informative"
	default_reading_level: str = "general"
	agno_cookbook_path: Optional[str] = None

	model_config = {
		"env_prefix": "BLOGGEN_",
		"case_sensitive": False,
	}


@lru_cache(maxsize=1)
def get_settings() -> Settings:
	return Settings()