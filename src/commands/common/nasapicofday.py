import discord
from discord import app_commands
from discord.ext import commands
from config import botConfig, config

import requests
from commands.utils.image_manipulation import image_manipulation as IM


class APOD(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="apod", description="Astronomy Picture of the Day")
    async def apod(self, interaction: discord.Interaction):
        await interaction.response.defer()

        response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={config["nasa-api-key"]}")
        apod_content = response.json()

        response = requests.get(apod_content["url"])

        hex_color = await IM._get_highest_frequency_color_hex(response=response)

        apod_embed = discord.Embed()

        apod_embed.title = apod_content["title"]
        apod_embed.description = apod_content["explanation"]
        apod_embed.set_footer(text=f"Copyright: {apod_content["copyright"]} | {apod_content["date"]}")
        apod_embed.set_image(url=apod_content["url"])
        apod_embed.color = int(hex_color.replace("#", ""), 16)
        
        await interaction.followup.send(embed=apod_embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(APOD(client=client), guild=discord.Object(id=botConfig["hub-server-guild-id"]))