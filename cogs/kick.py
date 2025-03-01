import discord
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def kick(self, ctx,  member: discord.Member, *args, reason="none"):
        embed = discord.Embed(description=f"> {member.mention} `kicked.`",
                              color=0x663300, timestamp=ctx.message.created_at)
        embed.set_author(name="Kicked", icon_url=member.avatar)
        embed.set_footer(text="Kicked", icon_url=member.avatar)
        embed.add_field(name="**ID:**",
                        value=f"> ```{member.id}```", inline=False)
        embed.add_field(
            name="**Name**", value=f"> {member.name}", inline=False)
        await ctx.send(embed=embed)
        await member.kick(reason=reason)


async def setup(bot: commands.Bot):
    await bot.add_cog(Kick(bot))
