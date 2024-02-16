import discord
from discord.ext import commands
import random
import os, asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command("help")

help_embed = discord.Embed(
    title="Bot Commands",
    description="Here are the available commands:",
    color=0x42F56C
)
help_embed.add_field(name=f"{bot.command_prefix}help", value="Displays all the available commands", inline=False)
help_embed.add_field(name=f"{bot.command_prefix}hello", value="Greets the user", inline=False)
help_embed.add_field(name=f"{bot.command_prefix}ping", value="Shows the bot's latency", inline=False)
help_embed.add_field(name=f"{bot.command_prefix}8ball <question>", value="Magic 8-Ball responses", inline=False)
    
@bot.event
async def on_ready():
        print("Bot is ready to use")

@bot.command()
async def hello(ctx):
    await ctx.send(f'👋 Hi, {ctx.author.mention}')

@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title="Pong! 🏓",
        description=f"Latency: {round(bot.latency * 1000)}ms",
        color=0x42F56C
    )
    await ctx.send(embed=embed)

@bot.command(aliases=["8ball"])
async def _8ball(ctx, *, questions):
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
        color=0x42F56C
    )
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
      await ctx.send(embed=help_embed)

bot.run(os.getenv("TOKEN"))