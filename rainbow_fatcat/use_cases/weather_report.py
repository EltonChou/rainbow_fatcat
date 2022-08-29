from datetime import datetime
from typing import List

from EorzeaEnv import (EorzeaLang, EorzeaPlaceName, EorzeaRainbow, EorzeaTime,
                       EorzeaWeather)
from rainbow_fatcat.entities import WeatherReport

RAINBOW_PERIOD_LIMIT = 500


def generate_weather_report(
    place_name: EorzeaPlaceName,
    lang: EorzeaLang = EorzeaLang.EN,
    count: int = 5
) -> List[WeatherReport]:
    reports = []
    the_rainbow = EorzeaRainbow(place_name=place_name)
    for et in EorzeaTime.weather_period(step=count):
        raw_weather = EorzeaWeather.forecast(
            place_name=place_name,
            timestamp=et,
            lang=lang,
            raw=True
        )
        the_rainbow.append(time=et, raw_weather=raw_weather)
        weather = EorzeaWeather.get_weather(raw_weather, lang)
        assert weather
        report = WeatherReport(
            time=datetime.fromtimestamp(et.get_unix_time()),
            weather=weather,
            has_rainbow=the_rainbow.is_appear
        )
        reports.append(report)
    return reports


def generate_rainbow_report(
    place_name: EorzeaPlaceName,
    lang: EorzeaLang = EorzeaLang.EN,
    count: int = 5
) -> List[WeatherReport]:
    reports = []
    the_rainbow = EorzeaRainbow(place_name=place_name)
    if the_rainbow.is_possible:
        count = 0
        for et in EorzeaTime.weather_period(step='inf'):
            raw_weather = EorzeaWeather.forecast(
                place_name=place_name,
                timestamp=et,
                lang=lang,
                raw=True
            )
            the_rainbow.append(time=et, raw_weather=raw_weather)
            weather = EorzeaWeather.get_weather(raw_weather, lang)
            assert weather
            if the_rainbow.is_appear:
                report = WeatherReport(
                    time=datetime.fromtimestamp(et.get_unix_time()),
                    weather=weather,
                    has_rainbow=the_rainbow.is_appear
                )
                reports.append(report)
            count += 1
            if len(reports) == 5 or count == RAINBOW_PERIOD_LIMIT:
                break

    return reports
