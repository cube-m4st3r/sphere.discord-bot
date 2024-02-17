import discord
from discord import app_commands
from discord.ext import commands
from config import botConfig, config

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

class WeatherStats(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="weatherstats", description="Show weather statistics")
    async def weatherstats(self, interaction: discord.Interaction):
        await interaction.response.defer()

        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 53.26,
            "longitude": 11.11,
            "hourly": ["temperature_2m", "relative_humidity_2m"],
            "timezone": "Europe/Berlin"
        }
        responses = openmeteo.weather_api(url, params=params)

        response = responses[0]

        weather_content = discord.Embed()
        weather_content.title = f"Weather Statistics"
        weather_content.add_field(name="Coordinates:", value=f"{response.Latitude()}°N {response.Longitude()}°E")
        weather_content.add_field(name="Elevation:", value=f"{response.Elevation()}m asl")
        weather_content.add_field(name="Timezone:", value=f"{response.Timezone()} {response.TimezoneAbbreviation()}")
        weather_content.add_field(name="Timezone difference to GMT+0:", value=f"{response.UtcOffsetSeconds()}s")


        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s"),
            end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )}
        hourly_data["temperature_2m"] = hourly_temperature_2m
        hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
        hourly_dataframe = pd.DataFrame(data = hourly_data)

        await interaction.followup.send(content=hourly_dataframe, embed=weather_content)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(WeatherStats(client=client), guild=discord.Object(id=botConfig["hub-server-guild-id"]))