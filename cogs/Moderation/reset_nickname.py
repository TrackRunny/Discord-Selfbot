import discord
import traceback
from discord.ext import commands
from logging_files.moderation_logging import logger


class ChangeNickname(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    async def resetnick(self, ctx, member: discord.Member):
        if ctx.guild.me.top_role < member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ User information",
                description="• The user has higher permissions than me!"
            )
            await ctx.send(embed=embed)
        elif ctx.author.top_role <= member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ User information",
                description="• The user has higher permissions than you or equal permissions!"
            )
            await ctx.send(embed=embed)
        elif ctx.guild.me.top_role > member.top_role:
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="• Resetnick Command",
                description=f"{member.mention}'s → Nickname has been **Reset!**"
            )

            await member.edit(nick=None)
            await ctx.send(embed=embed)

            logger.info(f"Moderation | Sent Reset Nickname: {ctx.author} | To: {member}")
        else:
            traceback.print_exc()

    @resetnick.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!resetnick @user`"
            )
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!resetnick @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Missing Permissions!",
                description="• You do not have permissions to run this command!"
            )

            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Missing Permissions",
                description="• You do not have permissions to run this command!"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                color=discord.Color.from_rgb(241, 90, 36),
                title="→ Bot Missing Permissions!",
                description="• Please give me permissions to use this command!"
            )
            await ctx.send(embed=embed)
        else:
            traceback.print_exc()


def setup(client):
    client.add_cog(ChangeNickname(client))
