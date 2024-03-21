import discord
from discord.ext import commands
from discord import app_commands
import datetime
import pytz

class luckybot(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="info", description="Shows server maintenance")
    async def info(self, interaction: discord.Interaction, server: str, reason: str):
        embed = discord.Embed(
            title="Server Maintenance",
            description="The server is undergoing maintenance",
            color=0xAD1717
        )
        embed.set_thumbnail(
            url="https://static.wikia.nocookie.net/minecraftid/images/3/3a/Lucky_Network.png/revision/latest?cb=20230103115650&path-prefix=id")
        embed.add_field(name="Affected Server", value=f"{server}", inline=False)
        embed.add_field(name="Time", value=f"{datetime.datetime.now(pytz.timezone('Asia/Jakarta'))}", inline=True)
        embed.add_field(name="Time Zone", value=f"{pytz.timezone('Asia/Jakarta')}", inline=True)
        embed.add_field(name="Reason",
                        value=f"{reason}",
                        inline=False)
        embed.set_footer(
            icon_url="https://static.wikia.nocookie.net/minecraftid/images/3/3a/Lucky_Network.png/revision/latest?cb=20230103115650&path-prefix=id",
            text="LuckyBot by LuckyStaff")
        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(luckybot(client))
