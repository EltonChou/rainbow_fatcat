from typing import Sequence, List

from discord import Embed
from EorzeaEnv import EorzeaPlaceName, EorzeaTime
from rainbow_fatcat.entities import WeatherReport


def generate_weather_forecast_embeds(
    place_name: EorzeaPlaceName,
    reports: Sequence[WeatherReport],
    rich_lt: bool = False
) -> Embed:
    report_strs: List[str] = []
    for report in reports:
        eorzea_datetime = EorzeaTime(report.time.timestamp())
        datetime_str = report.time.strftime("%m/%d %H:%M" if rich_lt else "%H:%M")
        rainbow_status = " :rainbow:" if report.has_rainbow else u""
        eorzea_time_str = f"`ET {eorzea_datetime.hour:02}:{eorzea_datetime.minute:02}`"
        local_time_str = f"`LT {datetime_str}`"
        report_str = f"**{report.weather}** {eorzea_time_str} {local_time_str} {rainbow_status}"
        report_strs.append(report_str)

    embed = Embed(title=place_name.value)
    embed.description = "\n".join(report_strs)
    return embed
