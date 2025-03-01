import discord
from discord.ext import commands


class PrivateChannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def pth(self, ctx):
        await ctx.channel.purge(limit=1)
        channel_mentions = ctx.message.channel_mentions

        if not channel_mentions:
            await ctx.send('```Please specify a channel tag.```')
            return

        channel = channel_mentions[0]

        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.read_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        embed = discord.Embed(
            description=f"<#{channel.id}> **The channel has been set to hidden mode.**", color=0xb106fa)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(PrivateChannel(bot))
