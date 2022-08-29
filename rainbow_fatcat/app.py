import os

import discord
from discord.app_commands import CommandTree

from rainbow_fatcat.use_cases.interaction import interaction_response
from rainbow_fatcat.use_cases.interaction_message import forecast

intents = discord.Intents.default()
client = discord.Client(intents=intents)
cmd_tree = CommandTree(client=client)


@client.event
async def on_ready():
    await client.wait_until_ready()
    await cmd_tree.sync()


@cmd_tree.command(description="Forecast the weather.")
async def weather(interaction: discord.Interaction, location: str, language: str = 'en'):
    msg = forecast(location=location, language=language)
    await interaction_response(interaction=interaction, message=msg)


@cmd_tree.command(description="Predict the rainbow.")
async def rainbow(interaction: discord.Interaction, location: str, language: str = 'en'):
    msg = forecast(location=location, language=language, rainbow_only=True)
    await interaction_response(interaction=interaction, message=msg)


def main():
    bot_secret = os.getenv('FATCAT_SECRET')
    if not bot_secret:
        raise ValueError("Can't get the `FATCAT_SECRET` environment variable.")

    client.run(bot_secret)


if __name__ == '__main__':
    main()
