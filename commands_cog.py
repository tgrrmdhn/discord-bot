import discord
from discord.ext import commands
import random

class commands_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command()
    async def hello(self, ctx):
        await ctx.send(f"👋 Hi, {ctx.author.mention}")
    @commands.hybrid_command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Pong! 🏓",
            description=f"Latency: {round(self.bot.latency * 1000)}ms",
            color=0x60E665
        )
        await ctx.send(embed=embed)
    @commands.hybrid_command(aliases=["8ball"])
    async def _8ball(self, ctx, *, questions):
        responses = ["It is certain",
                    "It is decidedly so",
                    "Without a doubt",
                    "Yes definitely",
                    "You may rely on it",
                    "As I see it, yes",
                    "Most likely",
                    "Outlook good",
                    "Yes",
                    "Signs point to yes",
                    "Reply hazy, try again",
                    "Ask again later",
                    "Better not tell you now",
                    "Cannot predict now",
                    "Concentrate and ask again",
                    "Don't count on it",
                    "My reply is no",
                    "My sources say no",
                    "Outlook not so good",
                    "Very doubtful"]
        response = random.choice(responses)
        embed = discord.Embed(
                    title="🎱 8-Ball",
                    description=f"Question : {questions}\nAnswer : {response}",
                    color=0x47E5ED
                )
        await ctx.send(embed=embed)