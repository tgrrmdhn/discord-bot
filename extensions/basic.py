import discord
from discord.ext import commands
from discord import app_commands
import random

class commands_cog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="hello", description="Greets the user")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"👋 Hi, {interaction.user.mention}")

    @app_commands.command(name="ping", description="Shows the latency")
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Pong! 🏓",
            description=f"Latency: {round(self.client.latency * 1000)}ms",
            color=0x60E665
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="8ball", description="Magic 8ball responses")
    async def _8ball(self, interaction: discord.Interaction, questions: str):
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
        await interaction.response.send_message(embed=embed)

async def setup(client) -> None:
    await client.add_cog(commands_cog(client))