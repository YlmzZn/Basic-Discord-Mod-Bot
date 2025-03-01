from discord.ext import commands


class Mat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def math(self, ctx, *, expression: str):
        calculation = eval(expression)
        await ctx.send(f'**Answer __{calculation}__**')


async def setup(bot: commands.Bot):
    await bot.add_cog(Mat(bot))
