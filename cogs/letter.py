from discord.ext import commands
from alf import *

class Letter(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def replace_letters(self, text, letters):
        replaced_text = ""
        for char in text:
            if char in letters:
                replaced_text += letters[char]
            else:
                replaced_text += char
        return replaced_text
    
    @commands.command()
    async def r(self, ctx, *, text):
        replaced_text = self.replace_letters(text, letters)
        await ctx.send(replaced_text)

async def setup(bot: commands.Bot):
    await bot.add_cog(Letter(bot))