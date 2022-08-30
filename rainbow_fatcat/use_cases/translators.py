from typing import Dict, Optional

from babel import parse_locale
from babel.support import Translations
from discord import Locale
from discord.app_commands import (TranslationContextTypes, Translator,
                                  locale_str)
from rainbow_fatcat.config import settings

translations: Dict[str, Translations] = {}


def get_translations(locale: Locale) -> Translations:
    language, territory, script, variant = parse_locale(locale.value, sep='-')
    if language in translations:
        return translations[language]
    return translations['en']


class CommandTranslator(Translator):
    async def load(self) -> None:
        for locale in settings.locales:
            translations[locale] = Translations.load(
                dirname=settings.locale_dir,
                locales=locale,
                domain='messages'
            )

    async def translate(
        self,
        string: locale_str,
        locale: Locale,
        context: TranslationContextTypes
    ) -> Optional[str]:
        t = get_translations(locale)
        t.install()
        return t.gettext(string.message)
