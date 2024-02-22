import discord
from discord.ext import commands
import asyncio
import os
from help_cog import help_cog
from commands_cog import commands_cog


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command("help")

async def main():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(commands_cog(bot))
        await bot.start(os.getenv("TOKEN"))

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot is ready to use")

asyncio.run(main())
