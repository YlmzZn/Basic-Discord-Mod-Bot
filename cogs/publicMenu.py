import discord
from discord.ext import commands
import paginator


class PublicMenu(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def command(self, ctx):

        img = "image url"

        embed = discord.Embed(color=0xc20000)

        embed.set_thumbnail(url=ctx.guild.icon)
        embed.set_image(url=img)

        embed.add_field(name="<**User info:**",
                        value="> ```.info + <@user> ```", inline=False)
        embed.add_field(name="**Server info**:",
                        value="> ```.server```", inline=False)
        embed.add_field(name="**Basic calculator:**",
                        value="> ```.math + {number1} + {+|-|*|/} + {number2}```", inline=False)
        embed.add_field(name="**Note reminder:**",
                        value="> ```.h + {time} + {note}```\n> ```second(s)|minute(m)|hour(h)|day(d)```\n>  __**Example:**__ `.h 5h join the server.`", inline=False)

        embed1 = discord.Embed(color=0xc20000)

        embed1.set_thumbnail(url=ctx.guild.icon)
        embed1.set_image(url=img)

        embed1.add_field(name="🪓 **Language abbreviations(For google translate)**",
                         value="> ```.lang```", inline=False)
        embed1.add_field(name="🔄 **Google Translate**",
                         value="> ```.translate {language abbreviations} {sentece}```", inline=False)

        embed2 = discord.Embed(color=0xc20000)

        embed2.set_thumbnail(url=ctx.guild.icon)
        embed2.set_image(url=img)

        embed2.add_field(name="**Memes:**",
                         value="> `.kilic + <@user>`\n> `.iskender + <@user>`\n> `.guray`\n> `.biat <@user>`\n> `.karahanli`\n> `.bedel`\n> `.laz <@user>`\n> `.büyük`\n> `.dogubey + <@user>`\n> `.son`\n> `.cerrahpasa`\n> `.ziya + <@user>`\n> `.cahil`\n> `.cahil2`\n> `.cahil3`\n> `.cahil4`\n> `.cahil5`", inline=False)

        embeds = [embed, embed1, embed2]

        await paginator.Simple(
            PreviousButton=discord.ui.Button(
                label="<", style=discord.ButtonStyle.red),
            NextButton=discord.ui.Button(
                label=">", style=discord.ButtonStyle.red),
            FirstButton=discord.ui.Button(
                label="<<", style=discord.ButtonStyle.red),
            LastButton=discord.ui.Button(
                label=">>", style=discord.ButtonStyle.red),
            PageCounterStyle=discord.ButtonStyle.red,
            InitialPage=0,
            timeout=42069).start(ctx, pages=embeds)


async def setup(bot: commands.Bot):
    await bot.add_cog(PublicMenu(bot))
