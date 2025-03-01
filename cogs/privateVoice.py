import discord
from discord.ext import commands


class PrivateVoice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def hvc(self, ctx, *, args):
        guild = ctx.guild
        ad = [args]
        x = (str(ad).replace('[', '').replace(']',
                                              '').replace("'", '').replace("'", ''))
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            ctx.author: discord.PermissionOverwrite(view_channel=True),
            guild.me: discord.PermissionOverwrite(view_channel=True)
        }

        await guild.create_voice_channel(f"{x}", overwrites=overwrites)
        embed = discord.Embed(
            description="**The hidden voice channel has been successfully created.**", color=0xb106fa)
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(PrivateVoice(bot))
