import discord
from discord.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def ban(self, ctx, user: discord.User):
        await ctx.guild.ban(user)
        embed = discord.Embed(description=f"> {user.mention} `banned.`",
                              color=0x660000, timestamp=ctx.message.created_at)
        embed.set_author(name="Banned", icon_url=user.avatar)
        embed.set_footer(text="Banned", icon_url=user.avatar)
        embed.add_field(name="**ID:**",
                        value=f"> ```{user.id}```", inline=False)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Ban(bot))
