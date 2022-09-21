from typing import Union

import discord


async def interaction_response(
    interaction: discord.Interaction, message: Union[str, discord.Embed]
):
    if type(message) is discord.Embed:
        await interaction.response.send_message(embed=message)
    if type(message) is str:
        await interaction.response.send_message(message)
