import discord
from discord.ext import commands
from discord import app_commands

class luckybot(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="maintenance", description="Shows server maintenance")
    async def maintenance(self, interaction: discord.Interaction, server: str, time: str, reason: str):
        embed = discord.Embed(
            title="Server Maintenance",
            description=f"Affected Server: {server}",
            color=0xAD1717
        )
        embed.add_field(name="Time", value=time, inline=True)
        embed.add_field(name="Reason", value=reason, inline=True)
        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(luckybot(client))
