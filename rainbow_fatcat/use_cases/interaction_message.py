from typing import Union

from discord import Embed, Locale

from .embeds import generate_weather_forecast_embeds
from .ensure_eorzeaenv import (
    ensure_eorzea_lang,
    ensure_place_name,
    ensure_rainbow_is_possible_in_location,
    LangMapping,
)
from .translators import get_translations
from .weather_report import generate_rainbow_report, generate_weather_report


def forecast(
    *, locale: Locale, location: str, language: str, rainbow_only: bool = False
) -> Union[Embed, str]:
    t = get_translations(locale)
    _ = t.gettext

    eorzea_lang = ensure_eorzea_lang(language)
    if eorzea_lang:
        place_name = ensure_place_name(location)
        if place_name:
            if rainbow_only:
                if ensure_rainbow_is_possible_in_location(place_name=place_name):
                    reports = generate_rainbow_report(
                        place_name=place_name, lang=eorzea_lang, count=5
                    )
                    if len(reports):
                        embed = generate_weather_forecast_embeds(
                            place_name=place_name, reports=reports, rich_lt=rainbow_only
                        )
                        return embed
                    return _("There is no rainbow in the future 500 weather cycles.")
                return _("The rainbow is impossible in") + f"`{place_name.value}`"

            reports = generate_weather_report(
                place_name=place_name, lang=eorzea_lang, count=5
            )
            embed = generate_weather_forecast_embeds(
                place_name=place_name, reports=reports, rich_lt=rainbow_only
            )
            return embed
        return f"`{location}` " + _("is not a valid place name.")
    return (
        ":warning:"
        + _("Supporting languages")
        + ": "
        + ", ".join(f"`{lang}`" for lang in LangMapping)
    )
