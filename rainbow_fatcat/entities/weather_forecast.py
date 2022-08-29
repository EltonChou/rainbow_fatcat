from datetime import datetime

from pydantic import BaseModel


class WeatherReport(BaseModel):
    time: datetime
    weather: str
    has_rainbow: bool
