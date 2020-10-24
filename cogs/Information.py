# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# LinuxBoi - Discord bot                                                    #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import asyncio
import time

import discord
import distro
import psutil
import platform
from discord.ext import commands

from logging_files.information_logging import logger


class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["commands", "cmds"])
    async def robot_commands(self, ctx):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ All available bot commands!",
            description="— "
                        "\n➤ Shows info about all available bot commands!"
                        "\n➤ Capitalization does not matter for the bot prefix." +
                        "\n—"
        )
        embed.set_thumbnail(url="https://i.imgur.com/BUlgakY.png")
        moderation = "`l!purge`, `l!warn`, `l!kick`, `l!ban`, `l!forceban`, `l!unban`," \
                     " `l!nickname`, `l!resetnick`, `l!addrole`, `l!delrole`"
        information = "`l!help`, `l!commands`, `l!ping`, `l!whois`, `l!server`,  `l!banner`, `l!invite`"
        fun = "`l!coinflip`, `l!avatar`, `l!howgay`, `l!8ball`, `l!dice`, `l!dadjoke`, `l!geekjoke`, " \
              "`l!cowsay`, `l!penguinsay`, `l!fortune`, `l!history`, `l!math`, `l!yo-momma-joke`, " \
              "`l!joke`, `l!chuck-norris`, `l!rps`, `l!advice`, `l!catfact`, `l!slot`, `l!question`, `l!bill`, " \
              "`l!foff`, `l!reverse`, `l!token`, `l!whalefact`, `l!koalafact`"
        utility = "`l!newsletter`, `l!poll`, `l!weather`, " \
                  "`l!mcpe`, `l!email`, `l!translate`, `l!bitly`, `l!hastebin`, `l!randomcolor`," \
                  " `l!bitcoin`, `l!tobtc`, `l!litecoin`, `l!currency`, " \
                  "`l!word random`, `l!word search`, `l!password`, `l!ip`, `l!remind`, `l!temperature fahrenheit`, " \
                  "`l!temperature celsius`, `l!uptime`"
        image = "`l!cat`, `l!dog`, `l!fox`, `l!bird`, `l!duck`, `l!tweet`," \
                "`l!trumptweet`, `l!captcha`, `l!clyde`, `l!vs`, `l!magik`, `l!threats`, `l!mind`, `l!ph`, `l!coffee`" \
                "`l!baguette`, `l!iphone`, `l!panda`, `l!youtube`, `l!triggered`"
        music = "`l!play`, `l!lyrics`, `l!pause`, `l!resume`, `l!skip`, `l!queue`, `l!np`, \
                 `l!volume`, `l!seek`, `l!shuffle`, `l!loop`, `l!search`, `l!stop`, `l!disconnect`"
        memes = "`l!meme`, `l!linuxmeme`, `l!windowsmeme`, `l!wikihow`, `l!dankmeme`, `l!programmermeme`, `l!edgymeme`, `l!darkmeme`"

        # linux_info = "`l!wheretostart`, `l!channels`"

        embed.add_field(name="• Moderation Commands!", inline=False, value=moderation)
        embed.add_field(name="• Information Commands!", inline=False, value=information)
        embed.add_field(name="• Fun Commands!", inline=False, value=fun)
        embed.add_field(name="• Memes!", inline=False, value=memes)
        embed.add_field(name="• Utility Commands!", inline=False, value=utility)
        embed.add_field(name="• Image Commands!", inline=False, value=image)
        embed.add_field(name="• Music Commands!", inline=False, value=music)
        # embed.add_field(name="• Linux information!", inline=False, value=linux_info)

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Commands: {ctx.author}")

    @commands.command()
    async def help(self, ctx):
        users = str(len(self.bot.users))
        guilds = str(len(self.bot.guilds))
        vote_link = "[**Vote link**](http://bit.ly/2mLoBOs) ⬆️"
        sourcecode_link = "[**Source Code**](https://github.com/TrackRunny/LinuxBoi) <:github:668680155807350792>"
        personal_website = "[**Personal Website**](https://trackrunny.codes) <:connection:678490219267489795>"
        cpu = str(psutil.cpu_percent())
        ram = str(psutil.virtual_memory()[3] / 1000000000)
        ram_round = ram[:3]
        disk = str(psutil.disk_usage('/')[1] / 1000000000)
        disk_round = disk[:4]
        boot_time = str(psutil.boot_time() / 100000000)
        boot_time_round = boot_time[:4]
        linux_distro = distro.os_release_info()
        get_news = self.bot.cursor.execute("SELECT rowid, * FROM bot_information")
        news = get_news.fetchall()[0][3]

        embed = discord.Embed(
            color=self.bot.embed_color,
            title=f"→ LinuxBoi",
            description=f"— "
                        f"\n ➤ Current news: {news}"
                        f"\n ➤ To view my commands run, `l!commands`"
                        f"\n ➤ Source code for this bot is available here: {sourcecode_link}"
                        f"\n ➤ If you like my bot, consider voting: {vote_link}"
                        f"\n ➤ My personal website: {personal_website}"
                        + "\n—"
        )
        embed.set_thumbnail(url="https://bit.ly/2JGhA94")
        embed.add_field(name=f"• OPERATING System:", inline=True, value=f":computer: — {linux_distro['pretty_name']}")
        embed.add_field(name=f"• CPU Usage:", inline=True, value=f":heavy_plus_sign: — {cpu} Percent used")
        embed.add_field(name=f"• RAM Usage:", inline=True,
                        value=f":closed_book:  —  {ram_round}  / 4  Gigabytes used")
        embed.add_field(name=f"• DISK Usage:", inline=True, value=f":white_circle: — {disk_round} / 40 Gigabytes")
        embed.add_field(name=f"• BOOT Time: ", inline=True, value=f":boot: —  {boot_time_round} seconds")
        embed.add_field(name=f"• MEMBER Count:", inline=True, value=f":bust_in_silhouette: —  {users} users")
        embed.add_field(name=f"• GUILD Count:", inline=True, value=f":house: — {guilds} connected guilds")
        embed.add_field(name=f"• LIBRARY Version:", inline=True, value=f":gear: — discord.py version {discord.__version__}")
        embed.add_field(name=f"• PYTHON Version:", inline=True, value=f":snake:  — Python version {platform.python_version()}")
        embed.set_footer(text=f"\n\nMade by TrackRunny#0001", icon_url=f"\n\nhttps://i.imgur.com/TiUqRH8.gif")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Help: {ctx.author}")

    @commands.command()
    async def invite(self, ctx):
        url = "(http://bit.ly/2Zm5XyP)"
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Invite Me To Your Server!",
            description=f"• [**Click Here**]{url}"
        )
        await ctx.message.add_reaction(self.bot.get_emoji(648198008076238862))

        await ctx.author.send(embed=embed)

        logger.info(f"Information | Sent Invite: {ctx.author}")

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        pong = int(round(self.bot.latency * 1000, 1))

        message = await ctx.send("• **Pong** — :ping_pong:")

        ping = (time.monotonic() - before) * 1000
        await message.delete(delay=1)
        await asyncio.sleep(1)

        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Ping Command",
        )
        embed.add_field(name="• WS:", value=f"{pong}ms")
        embed.add_field(name="• REST:", value=f"{int(ping)}ms")
        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Ping: {ctx.author}")

    @commands.command(aliases=['server'])
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(
            color=self.bot.embed_color,
            title=f"→ Server Info For {guild.name}",
            description="\n— "
                        "\n➤ Shows all information about a guild."
                        "\n➤The information will be listed below!"
                        "\n —"
        )
        regions = {
            "us_west": ":flag_us: — USA West",
            "us_east": ":flag_us: — USA East",
            "us_central": ":flag_us: — USA Central",
            "us_south": ":flag_us: — USA South",
            "sydney": ":flag_au: — Sydney",
            "eu_west": ":flag_eu: — Europe West",
            "eu_east": ":flag_eu: — Europe East",
            "eu_central": ":flag_eu: — Europe Central",
            "singapore": ":flag_sg: — Singapore",
            "russia": ":flag_ru: — Russia",
            "southafrica": ":flag_za:  — South Africa",
            "japan": ":flag_jp: — Japan",
            "brazil": ":flag_br: — Brazil",
            "india": ":flag_in: — India",
            "hongkong": ":flag_hk: — Hong Kong",
        }
        verifications = {
            "none": "<:white__circle:625695417782239234> — No Verification",
            "low": "<:green_circle:625541294525251643> — Low Verification",
            "medium": "<:yellow_circle:625540435820937225> — Medium Verification",
            "high": "<:orange_circle:625542217100165135> — High Verification",
            "extreme": "<:red__circle:625833379258040330> — Extreme Verification"
        }
        embed.set_thumbnail(url=guild.icon_url_as(size=1024, format=None, static_format="png"))
        embed.add_field(name="• Guild name: ", value=str(guild.name))
        embed.add_field(name="• Guild ID: ", value=str(guild.id))
        embed.add_field(name="• Guild owner: ", value=guild.owner)
        embed.add_field(name="• Guild owner ID: ", value=guild.owner_id)
        embed.add_field(name="• Guild made in: ", value=guild.created_at.strftime("%A %d, %B %Y"))
        embed.add_field(name="• Channels count: ", value=len(guild.channels))
        embed.add_field(name="• Guild region: ", value=regions[guild.region.name])
        embed.add_field(name="• Guild verification: ", value=verifications[guild.verification_level.name])
        embed.add_field(name="• Member count: ", value=f"{guild.member_count}")
        embed.add_field(name="• Nitro boosters: ", value=guild.premium_subscription_count or "No Nitro Boosters!")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Serverinfo : {ctx.author}")

    @commands.command(aliases=['banner'])
    async def server_banner(self, ctx):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title="→ Server Banner",
        )
        embed.set_image(url=ctx.guild.icon_url_as(size=1024, format=None, static_format="png"))

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Banner: {ctx.author}")

    @commands.command(aliases=['userinfo'])
    async def whois(self, ctx, member: discord.Member):
        embed = discord.Embed(
            color=self.bot.embed_color,
            title=f"→ Userinfo For {member}",
            description="— "
                        "\n➤ Shows all information about a user. "
                        "\n➤ The information will be listed below!"
                        "\n —"
        )

        status = {
            "online": "<:online:648195346186502145>",
            "idle": "<:idle:648195345800757260>",
            "offline": "<:offline:648195346127912970>",
            "dnd": "<:dnd:648195345985175554>"
        }

        roles = [role for role in member.roles]
        roles = f" ".join([f"`@{role}`, " for role in roles])

        embed.set_thumbnail(url=member.avatar_url_as(size=1024, format=None, static_format="png"))
        embed.add_field(name="• Account name: ", value=str(member))
        embed.add_field(name="• Discord ID: ", value=str(member.id))
        embed.add_field(name="• Nickname: ", value=member.nick or "No nickname!")
        embed.add_field(name="• Account created at: ", value=member.created_at.strftime("%A %d, %B %Y."))
        embed.add_field(name="• Account joined at: ", value=member.joined_at.strftime("%A %d, %B %Y"))

        # - TODO: See why this is returning "None" even though there is an if statement to check this
        if member.activity is None:
            embed.add_field(name="• Activity: ", value="No activity!")
        else:
            embed.add_field(name="• Activity: ", value=member.activity.name)
        if member.bot is True:
            embed.add_field(name="• Discord bot? ", value="<:bot_tag:648198074094583831> = <:tick_yes:648198008076238862>")
        else:
            embed.add_field(name="• Discord bot?", value="<:bot_tag:648198074094583831> = <:tick_no:648198035435945985>")
        if member.is_on_mobile() is True:
            embed.add_field(name="• On mobile? ", value=":iphone:")
        else:
            embed.add_field(name="• On mobile? ", value=":no_mobile_phones:")

        embed.add_field(name="• Status: ", value=status[member.status.name])
        embed.add_field(name="• Top role: ", value=f"`@{member.top_role}`")
        embed.add_field(name="• Roles: ", inline=False, value=roles)

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Whois: {ctx.author}")

    @whois.error
    async def whois_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Member!",
                description="• Please mention a valid member! Example: `l!whois @user`"
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=self.bot.embed_color,
                title="→ Invalid Argument!",
                description="• Please put a valid option! Example: `l!whois @user`"
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
