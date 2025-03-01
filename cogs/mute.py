import discord
from discord.ext import commands


class Mute(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def mute(self, ctx, member: discord.Member):
        embed = discord.Embed(
            description=f"{member.mention}, **has muted.**", colour=0xff0000)
        mute_role_id = 34532426
        muteRole = discord.utils.get(ctx.guild.roles, id=mute_role_id)
        await member.add_roles(muteRole)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Mute(bot))
