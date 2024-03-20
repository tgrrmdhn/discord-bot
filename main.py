import asyncio
import logging
import logging.handlers
from typing import Optional
from aiohttp import ClientSession
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()


class projectA(commands.Bot):
    def __init__(
            self,
            *args,
            web_client: ClientSession,
            testing_guild_id: Optional[int]=None,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.web_client = web_client
        self.testing_guild_id = testing_guild_id

    async def setup_hook(self) -> None:
        for filename in os.listdir("./extensions"):
            if filename.endswith(".py"):
                await self.load_extension(f"extensions.{filename[:-3]}")
        if self.testing_guild_id:
            guild = discord.Object(self.testing_guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)

async def main():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32*1024*1024,
        backupCount=5
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    async with ClientSession() as our_client:
        intents = discord.Intents.default()
        intents.message_content = True
        async with projectA(
            commands.when_mentioned,
            web_client=our_client,
            intents=intents
        ) as bot:
            bot.remove_command('help')
            await bot.start(os.getenv('TOKEN'))

asyncio.run(main())
