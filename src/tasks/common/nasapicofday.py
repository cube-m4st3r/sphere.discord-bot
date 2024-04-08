import discord

import aiohttp
from utils.image_manipulation import image_manipulation as IM

async def get_nasapicoftheday():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://127.0.0.1:8000/nasa/apod/get_latest_post", ssl=False) as response:
                response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
                apod_content = await response.json()

                async with session.get(apod_content["url"]) as image_response:
                    image_response.raise_for_status()
                    image_data = await image_response.read()

                hex_color = await IM._get_highest_frequency_color_hex(image_data=image_data)

                apod_embed = discord.Embed()

                apod_embed.title = apod_content["title"]
                apod_embed.description = apod_content["explanation"]
                if "copyright" in apod_content:
                    apod_embed.set_footer(text=f"Copyright: {apod_content['copyright']} | {apod_content['date']}")
                apod_embed.set_footer(text=f"{apod_content['date']}")
                apod_embed.set_image(url=apod_content["url"])
                apod_embed.color = int(hex_color.replace("#", ""), 16)

                return apod_embed
    except aiohttp.ClientError as e:
        print(f"Error making HTTP request: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

