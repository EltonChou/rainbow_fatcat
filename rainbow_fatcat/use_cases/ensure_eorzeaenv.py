from typing import Optional

from EorzeaEnv import EorzeaLang, EorzeaPlaceName, EorzeaRainbow
from EorzeaEnv.errors import EorzeaEnvError, InvalidEorzeaPlaceName


def ensure_place_name(place_name: str) -> Optional[EorzeaPlaceName]:
    try:
        eorzea_location = EorzeaPlaceName(
            place_name=place_name,
            strict=False
        )
    except InvalidEorzeaPlaceName:
        return None

    except EorzeaEnvError:
        return None

    return eorzea_location


LangMapping = {
    'en': EorzeaLang.EN,
    'ja': EorzeaLang.JA,
    'de': EorzeaLang.DE,
    'fr': EorzeaLang.FR
}


def ensure_eorzea_lang(language: str) -> Optional[EorzeaLang]:
    return LangMapping[language] if language in LangMapping else None


def ensure_rainbow_is_possible_in_location(place_name: EorzeaPlaceName) -> bool:
    rainbow = EorzeaRainbow(place_name=place_name)
    return rainbow.is_possible
