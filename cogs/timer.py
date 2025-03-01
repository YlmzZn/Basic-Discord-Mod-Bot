import discord
from discord.ext import commands
from discord.ui import Button, View
from typing import Optional
import humanfriendly
import time as pyTime
import asyncio


class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def h(self, ctx, time, *, args: Optional[str]):
        times = humanfriendly.parse_timespan(time)
        epoch = pyTime.time() + times
        await ctx.channel.purge(limit=1)
        channel = ctx.channel
        my_msg = await ctx.channel.send(f"> <t:{int(epoch)}:f> <t:{int(epoch)}:R> **I will remind you.**")
        d = time[-1]

        num = int(time[:-1])

        if d == "s":
            await asyncio.sleep(num)

        if d == "m":
            await asyncio.sleep(num * 60)

        if d == "h":
            await asyncio.sleep(num * 60 * 60)

        if d == "d":
            await asyncio.sleep(num * 60 * 60 * 24)

        button_url = f"https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{my_msg.id}"
        button = Button(label="The channel where you used the reminder.",
                        url=button_url, emoji="📌")
        view = View()
        view.add_item(button)

        user = await self.bot.fetch_user(ctx.author.id)
        embed = discord.Embed(
            description=f"<t:{int(epoch)}:f>", color=0xc20000)
        embed.add_field(name="__**Remind time**__",
                        value=f"> • {args}", inline=False)
        await user.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Timer(bot))
