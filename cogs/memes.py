import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO


class Members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kilic(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("img/kılıç3.png")
        asset = user.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((177, 177))
        wanted.paste(pfp, (710, 15))
        wanted.save("img/profile.png")
        await ctx.send(file=discord.File("img/profile.png"))

    @commands.command()
    async def ziya(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("img/atma.png")
        asset = user.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((140, 140))
        wanted.paste(pfp, (440, 120))
        wanted.save("img/profile.png")
        await ctx.send(file=discord.File("img/profile.png"))

    @commands.command()
    async def iskender(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("img/iskenderp.png")
        asset = user.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((34, 34))
        wanted.paste(pfp, (145, 78))
        wanted.save("img/görüntü.png")
        await ctx.send(file=discord.File("img/görüntü.png"))

    @commands.command()
    async def dogubey(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("img/doğubey.png")
        asset = user.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((100, 100))
        wanted.paste(pfp, (366, 70))
        wanted.save("img/görüntü.png")
        await ctx.send(file=discord.File("img/görüntü.png"))

    @commands.command()
    async def guray(self, ctx):
        with open("img/güray.png", "rb") as fh:
            f = discord.File(fh, filename="img/güray.png")
        await ctx.send(file=f)

    @commands.command()
    async def son(self, ctx):
        with open("img/son.png", "rb") as fh:
            f = discord.File(fh, filename="img/son.png")
        await ctx.send(file=f)

    @commands.command()
    async def cerrahpasa(self, ctx):
        with open("img/cerrah.png", "rb") as fh:
            f = discord.File(fh, filename="img/cerrah.png")
        await ctx.send(file=f)

    @commands.command()
    async def karahanli(self, ctx):
        with open("img/karahanlıı.png", "rb") as fh:
            f = discord.File(fh, filename="img/karahanlıı.png")
        await ctx.send(file=f)

    @commands.command()
    async def bedel(self, ctx):
        with open("img/bedell.png", "rb") as fh:
            f = discord.File(fh, filename="img/bedell.png")
        await ctx.send(file=f)

    @commands.command()
    async def biat(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("img/biatet.png")
        asset = user.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((171, 164))
        wanted.paste(pfp, (592, 599))
        wanted.save("img/görüntü.png")
        await ctx.send(file=discord.File("img/görüntü.png"))

    @commands.command()
    async def laz(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("img/ziya.png")
        asset = user.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((263, 243))
        wanted.paste(pfp, (871, 417))
        wanted.save("img/görüntü.png")
        await ctx.send(file=discord.File("img/görüntü.png"))

    @commands.command()
    async def buyuk(self, ctx):
        with open("img/büyükk.png", "rb") as fh:
            f = discord.File(fh, filename="img/büyükk.png")
        await ctx.send(file=f)

    @commands.command()
    async def cahil(self, ctx):
        with open("img/cahil.png", "rb") as fh:
            f = discord.File(fh, filename="img/cahil.png")
        await ctx.send(file=f)

    @commands.command()
    async def cahil1(self, ctx):
        with open("img/cahil1.png", "rb") as fh:
            f = discord.File(fh, filename="img/cahil1.png")
        await ctx.send(file=f)

    @commands.command()
    async def cahil2(self, ctx):
        with open("img/cahil2.png", "rb") as fh:
            f = discord.File(fh, filename="img/cahil2.png")
        await ctx.send(file=f)

    @commands.command()
    async def cahil3(self, ctx):
        with open("img/cahil3.png", "rb") as fh:
            f = discord.File(fh, filename="img/cahil3.png")
        await ctx.send(file=f)

    @commands.command()
    async def cahil4(self, ctx):
        with open("img/cahil4.png", "rb") as fh:
            f = discord.File(fh, filename="img/cahil4.png")
        await ctx.send(file=f)

    @commands.command()
    async def cahil5(self, ctx):
        with open("img/cahil5.png", "rb") as fh:
            f = discord.File(fh, filename="img/cahil5.png")
        await ctx.send(file=f)


async def setup(bot):
    await bot.add_cog(Members(bot))
