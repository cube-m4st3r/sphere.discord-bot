import discord 
from discord import app_commands
from discord.ext import commands
from config import botConfig, config
from utils.anime_loader import load_full_anime_show
from datetime import datetime


class AnimeGroup(app_commands.Group):
    @app_commands.command(description="Search for a specific anime")
    async def search(self, interaction: discord.Interaction, input: str):
        await interaction.response.defer()

        await interaction.followup.send(embed=await build_anime_embed(anime=await load_full_anime_show(title=input)))


async def build_anime_embed(anime):
    themes = anime.theme
    genres = anime.genre
    formatted_themes = ", ".join(theme.name for theme in themes)
    formatted_genres = ", ".join(genre.name for genre in genres)

    aired_start_clean = anime.aired_start.split('.')[0]
    aired_end_clean = anime.aired_end.split('.')[0]

    anime_embed = discord.Embed()
    anime_embed.title = f"{anime.title}"
    anime_embed.add_field(name="Type:", value=f"{anime.type}")
    anime_embed.add_field(name="Episodes:", value=f"{anime.episodes_amount}")
    anime_embed.add_field(name="Status:", value=f"{anime.status}")
    anime_embed.add_field(name="Aired:", value=f"From: {datetime.strptime(aired_start_clean, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y @ %H:%M:%S')}\nTo: {datetime.strptime(aired_end_clean, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y @ %H:%M:%S')}")
    anime_embed.add_field(name="Premiered:", value=f"{anime.premiered}")
    anime_embed.add_field(name="Broadcast:", value=f"{anime.broadcast}")
    anime_embed.add_field(name="Source:", value=f"{anime.source}")
    anime_embed.add_field(name="Themes:", value=f"{formatted_themes}")
    anime_embed.add_field(name="Genres:", value=f"{formatted_genres}")

    return anime_embed

class Anime(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    anime_group = AnimeGroup(name="anime", description="Anime related commands.")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Anime(client=client), guild=discord.Object(id=botConfig["hub-server-guild-id"]))