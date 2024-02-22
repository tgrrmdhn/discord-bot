import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_embed = None
        self.set_embed()
    def set_embed(self):
        self.help_embed = discord.Embed(
            title="Bot Commands",
            description="List of commands",
            color=0x47E5ED
        )
        self.help_embed.add_field(name=f"{self.bot.command_prefix}help", value="Displays all the available commands", inline=False)
        self.help_embed.add_field(name=f"{self.bot.command_prefix}hello", value="Greets the user", inline=False)
        self.help_embed.add_field(name=f"{self.bot.command_prefix}ping", value="Shows the latency", inline=False)
        self.help_embed.add_field(name=f"{self.bot.command_prefix}8ball <question>", value="Magic 8-Ball responses", inline=False)
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status(f"/help or {self.bot.command_prefix}help | by @asianpingissue"))
    @commands.hybrid_command()
    async def help(self, ctx):
        await ctx.send(embed=self.help_embed)