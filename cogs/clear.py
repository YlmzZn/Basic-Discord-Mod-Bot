import discord
from discord.ext import commands
from typing import Optional

class Clear(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def cls(self, ctx, member: Optional[discord.Member], amount: int = 5):
        def _check(message):
            if member is None:
                return True
            else:
                if message.author != member:
                    return False
                _check.count += 1
                return _check.count <= amount
        _check.count = 0
        await ctx.channel.purge(limit=amount + 1 if member is None else 1000, check=_check)

async def setup(bot: commands.Bot):
    await bot.add_cog(Clear(bot))
