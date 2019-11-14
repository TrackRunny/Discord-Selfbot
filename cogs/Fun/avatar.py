import discord
from logging_files.fun_logging import logger
from discord.ext import commands


class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=discord.Color.from_rgb(241, 90, 36),
            title="→ Avatar"
        )
        embed.set_image(url=member.avatar_url_as(size=4096, format=None, static_format="png"))

        await ctx.send(embed=embed)

        logger.info(f"Fun | Sent Avatar: {ctx.author}")

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!avatar @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument",
                description="• Please put a valid option! Example: `l!avatar @user`"
            )
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Avatar(client))
