from pathlib import Path
from typing import Sequence

from pydantic import BaseSettings, DirectoryPath, Field


class Settings(BaseSettings):
    secret: str = Field(..., env="FATCAT_SECRET")
    locales: Sequence[str] = ["en", "ja", "zh"]
    locale_dir: DirectoryPath = Path(__file__).parent.joinpath("locale").absolute()
    activity: str = "with rainbow"


settings = Settings()  # type: ignore
