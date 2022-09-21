import discord
from discord.app_commands import CommandTree
from discord.app_commands import locale_str as _

from rainbow_fatcat.config import settings
from rainbow_fatcat.use_cases.interaction import interaction_response
from rainbow_fatcat.use_cases.interaction_message import forecast
from rainbow_fatcat.use_cases.translators import CommandTranslator

intents = discord.Intents.default()
client = discord.Client(intents=intents)
cmd_tree = CommandTree(client=client)


@client.event
async def on_ready():
    await client.wait_until_ready()
    await cmd_tree.set_translator(CommandTranslator())
    await cmd_tree.sync()
    await client.change_presence(activity=discord.Game(name=settings.activity))


@cmd_tree.command(description=_("Forecast the weather."))
async def weather(
    interaction: discord.Interaction, location: str, language: str = "en"
):
    msg = forecast(locale=interaction.locale, location=location, language=language)
    await interaction_response(interaction=interaction, message=msg)


@cmd_tree.command(description=_("Predict the rainbow appearing time."))
async def rainbow(
    interaction: discord.Interaction, location: str, language: str = "en"
):
    msg = forecast(
        locale=interaction.locale,
        location=location,
        language=language,
        rainbow_only=True,
    )
    await interaction_response(interaction=interaction, message=msg)


def main():
    client.run(settings.secret)


if __name__ == "__main__":
    main()
