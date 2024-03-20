import discord
from discord.ext import commands
from discord import app_commands

class help_cog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.help_embed = None
        self.set_embed()
    def set_embed(self):
        self.help_embed = discord.Embed(
            title="Bot Commands",
            description="List of commands",
            color=0x47E5ED
        )
        self.help_embed.add_field(name=f"/help", value="Displays all the available commands", inline=False)
        self.help_embed.add_field(name=f"/hello", value="Greets the user", inline=False)
        self.help_embed.add_field(name=f"/ping", value="Shows the latency", inline=False)
        self.help_embed.add_field(name=f"/8ball <question>", value="Magic 8-Ball responses", inline=False)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(f"/help | by @dominator1537"))

    @app_commands.command(name="maintenance", description="Shows server maintenance")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=self.help_embed)

async def setup(client) -> None:
    await client.add_cog(help_cog(client))