import discord 
from discord import app_commands
from discord.ext import commands
from config import botConfig, config
from datetime import datetime
import aiohttp
from config import config
from Classes.animeShow import AnimeShow


class AnimeGroup(app_commands.Group):
    @app_commands.command(description="Search for a specific anime")
    async def search(self, interaction: discord.Interaction, input: str):
        await interaction.response.defer()
        
        anime, db = await load_full_anime_show(title=input)
        if anime is None:
            await interaction.followup.send(embed=discord.Embed(title="Error", description="No anime found with that title."))
            return

        embed = await build_anime_embed(anime=anime)
        if db:
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send(embed=embed, view=AddToDB())


async def load_full_anime_show(title):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{config["backend_url"]}/api/anime_shows', params={'title': title}, ssl=False) as response:
                if response.status != 200:
                    print(f"Error: Received a {response.status} status code.")
                    return None
                
                try:
                    data = await response.json()
                except aiohttp.ContentTypeError as e:
                    print(f"Error parsing JSON: {e}")
                    return 

                if data:
                    return AnimeShow(data=data[0]), True
                else: 
                    return 

    except aiohttp.ClientError as e:
        print(f"HTTP request failed: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


class AddToDBButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Add", style=discord.ButtonStyle.primary, emoji="<:db_icon:1266681564368994314>")
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("test")

class AddToDB(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(AddToDBButton())


async def build_anime_embed(anime):
    themes = anime.theme
    genres = anime.genre
    formatted_themes = ", ".join(theme.name for theme in themes)
    formatted_genres = ", ".join(genre.name for genre in genres)

    #aired_start_clean = anime.aired_start.split('.')[0]
    #aired_end_clean = anime.aired_end.split('.')[0]

    anime_embed = discord.Embed()
    anime_embed.title = f"{anime.title}"
    anime_embed.add_field(name="Type:", value=f"{anime.type}")
    anime_embed.add_field(name="Episodes:", value=f"{anime.episodes_amount}")
    anime_embed.add_field(name="Status:", value=f"{anime.status}")
    anime_embed.add_field(name="Aired:", value=f"From: {anime.aired_start}\nTo: {anime.aired_end}", inline=False)
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