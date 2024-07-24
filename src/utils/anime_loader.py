from Classes.animeShow import AnimeShow
from Classes.animeThemes import AnimeTheme
from Classes.animeGenres import AnimeGenre
import aiohttp
from config import config

async def load_anime_genre(data: dict):
    genres = list()
    for genre in data:
        genres.append(AnimeGenre(data=genre))
    return genres


async def load_anime_theme(data: dict):
    themes = list()
    for theme in data:
        themes.append(AnimeTheme(data=theme))
    return themes


async def load_anime_show(data: dict):
    return AnimeShow(data=data)


async def load_full_anime_show(title):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{config["backend_url"]}/anime/search', params={'q': title}, ssl=False) as response:
            if response.status == 200:
                data = await response.json()
                return await load_anime_show(data=data)
                # empty constructor anime show, list appending of animetheme and genre