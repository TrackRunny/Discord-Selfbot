import discord
from discord.ext import commands
from logging_files.utility_logging import logger

class Temperatures(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=["temp"], invoke_without_command=True)
    async def temperature(self, ctx):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Invalid Argument!",
            description="• Please put in a valid option! Example: `l!temperature <fahrenheit / celsius> <number>`"
        )

        await ctx.send(embed=embed)

    @temperature.command(aliases=["fahrenheit"])
    async def fahrenheit_to_celsius(self, ctx, fahrenheit):
        celsius = (int(fahrenheit) - 32) * 5 / 9
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Fahrenheit to Celsius",
            description=f"• Celsius Temperature: `{int(celsius)}`"
        )
        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Temperatures: {ctx.author}")

    @temperature.command(aliases=["celsius"])
    async def celsius_to_fahrenheit(self, ctx, celsius):
        fahrenheit = (int(celsius) * 9 / 5) + 32
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Celsius to Fahrenheit",
            description=f"• Fahrenheit Temperature: `{int(fahrenheit)}`"
        )

        await ctx.send(embed=embed)

        logger.info(f"Utility | Sent Temperatures: {ctx.author}")


def setup(client):
    client.add_cog(Temperatures(client))


