import discord 
from discord import app_commands
from discord.ext import commands
from config import botConfig, config
from utils.anime_loader import load_full_anime_show


class AnimeGroup(app_commands.Group):
    @app_commands.command(description="Search for a specific anime")
    async def search(self, interaction: discord.Interaction, input: str):
        await interaction.response.defer()

        show = await load_full_anime_show(title=input)


class Anime(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    anime_group = AnimeGroup(name="anime", description="Anime related commands.")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Anime(client=client), guild=discord.Object(id=botConfig["hub-server-guild-id"]))