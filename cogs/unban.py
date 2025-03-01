import discord
from discord.ext import commands


class Unban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def unban(self, ctx, user: discord.User):
        await ctx.guild.unban(user)
        embed = discord.Embed(
            description=f"{user.mention} has unbanned.", color=0xFF9999)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Unban(bot))
