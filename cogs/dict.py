import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import googletrans
import paginator


class Dict(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lang_icon_url = ""
        self.lang_thumbnail = ""
        self.lang_image = ""

    # Google translate
    @commands.command()
    async def translate(self, ctx, lang_to, *args):
        lang_to = lang_to.lower()
        if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODES:
            raise commands.BadArgument("```Invalid spelling!```")

        text = ' '.join(args)
        translator = googletrans.Translator()
        text_translated = translator.translate(text, dest=lang_to).text
        embed = discord.Embed(
            description=f"> • {text_translated}", color=0xc20000)
        embed.set_author(
            name="Google Translate", icon_url="")
        await ctx.reply(embed=embed)

    # Language abbreviations
    @commands.command()
    async def lang(self, ctx):
        d1 = discord.Embed(color=0x00ff00)

        d1.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d1.set_thumbnail(url=self.lang_thumbnail)
        d1.set_image(url=self.lang_image)

        d1.add_field(name="🔺 af",
                     value="`afrikaans`", inline=True)
        d1.add_field(name="🔺 sq",
                     value="`albanian`", inline=True)
        d1.add_field(name="🔺 am",
                     value="`amharic`", inline=True)
        d1.add_field(name="🔺 ar",
                     value="`arabic`", inline=True)
        d1.add_field(name="🔺 hy",
                     value="`armenian`", inline=True)
        d1.add_field(name="🔺 az",
                     value="`azerbaijani`", inline=True)
        d1.add_field(name="🔺 eu",
                     value="`basque`", inline=True)
        d1.add_field(name="🔺 be",
                     value="`belarusian`", inline=True)
        d1.add_field(name="🔺 bn",
                     value="`bengali`", inline=True)
        d1.add_field(name="🔺 bs",
                     value="`bosnian`", inline=True)

        d2 = discord.Embed(color=0x00ff00)

        d2.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d2.set_thumbnail(url=self.lang_thumbnail)
        d2.set_image(url=self.lang_image)

        d2.add_field(name="🔺 bg",
                     value="`bulgarian`", inline=True)
        d2.add_field(name="🔺 ca",
                     value="`catalan`", inline=True)
        d2.add_field(name="🔺 ceb",
                     value="`cebuano`", inline=True)
        d2.add_field(name="🔺 ny",
                     value="`chichewa`", inline=True)
        d2.add_field(name="🔺 zh-cn",
                     value="`chinese (simplified)`", inline=True)
        d2.add_field(name="🔺 zh-tw",
                     value="`chinese (traditional)`", inline=True)
        d2.add_field(name="🔺 co",
                     value="`corsican`", inline=True)
        d2.add_field(name="🔺 hr",
                     value="`croatian`", inline=True)
        d2.add_field(name="🔺 cs",
                     value="`czech`", inline=True)
        d2.add_field(name="🔺 da",
                     value="`danish`", inline=True)

        d3 = discord.Embed(color=0x00ff00)

        d3.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d3.set_thumbnail(url=self.lang_thumbnail)
        d3.set_image(url=self.lang_image)

        d3.add_field(name="🔺 nl",
                     value="`dutch`", inline=True)
        d3.add_field(name="🔺 en",
                     value="`english`", inline=True)
        d3.add_field(name="🔺 eo",
                     value="`esperanto`", inline=True)
        d3.add_field(name="🔺 et",
                     value="`estonian`", inline=True)
        d3.add_field(name="🔺 tl",
                     value="`filipino`", inline=True)
        d3.add_field(name="🔺 fi",
                     value="`finnish`", inline=True)
        d3.add_field(name="🔺 fr",
                     value="`french`", inline=True)
        d3.add_field(name="🔺 fy",
                     value="`frisian`", inline=True)
        d3.add_field(name="🔺 gl",
                     value="`galician`", inline=True)
        d3.add_field(name="🔺 ka",
                     value="`georgian`", inline=True)

        d4 = discord.Embed(color=0x00ff00)

        d4.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d4.set_thumbnail(url=self.lang_thumbnail)
        d4.set_image(url=self.lang_image)

        d4.add_field(name="🔺 de",
                     value="`german`", inline=True)
        d4.add_field(name="🔺 el",
                     value="`greek`", inline=True)
        d4.add_field(name="🔺 gu",
                     value="`gujarati`", inline=True)
        d4.add_field(name="🔺 ht",
                     value="`haitian creole`", inline=True)
        d4.add_field(name="🔺 ha",
                     value="`hausa`", inline=True)
        d4.add_field(name="🔺 haw",
                     value="`hawaiian`", inline=True)
        d4.add_field(name="🔺 iw",
                     value="`hebrew`", inline=True)
        d4.add_field(name="🔺 he",
                     value="`hebrew`", inline=True)
        d4.add_field(name="🔺 hi",
                     value="`hindi`", inline=True)
        d4.add_field(name="🔺 hmn",
                     value="`hmong`", inline=True)

        d5 = discord.Embed(color=0x00ff00)

        d5.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d5.set_thumbnail(url=self.lang_thumbnail)
        d5.set_image(url=self.lang_image)

        d5.add_field(name="🔺 hu",
                     value="`hungarian`", inline=True)
        d5.add_field(name="🔺 is",
                     value="`icelandic`", inline=True)
        d5.add_field(name="🔺 ig",
                     value="`igbo`", inline=True)
        d5.add_field(name="🔺 id",
                     value="`indonesian`", inline=True)
        d5.add_field(name="🔺 ga",
                     value="`irish`", inline=True)
        d5.add_field(name="🔺 it",
                     value="`italian`", inline=True)
        d5.add_field(name="🔺 ja",
                     value="`japanese`", inline=True)
        d5.add_field(name="🔺 jw",
                     value="`javanese`", inline=True)
        d5.add_field(name="", value="", inline=True)
        d5.add_field(name="", value="", inline=True)

        d6 = discord.Embed(color=0x00ff00)

        d6.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d6.set_thumbnail(url=self.lang_thumbnail)
        d6.set_image(url=self.lang_image)

        d6.add_field(name="🔺 kn",
                     value="`kannada`", inline=True)
        d6.add_field(name="🔺 kk",
                     value="`kazakh`", inline=True)
        d6.add_field(name="🔺 km",
                     value="`khmer`", inline=True)
        d6.add_field(name="🔺 ko",
                     value="`korean`", inline=True)
        d6.add_field(name="🔺 ku",
                     value="`kurdish (kurmanji)`", inline=True)
        d6.add_field(name="🔺 ky",
                     value="`kyrgyz`", inline=True)
        d6.add_field(name="🔺 lo",
                     value="`lao`", inline=True)
        d6.add_field(name="🔺 la",
                     value="`latin`", inline=True)
        d6.add_field(name="🔺 lv",
                     value="`latvian`", inline=True)
        d6.add_field(name="🔺 lt",
                     value="`lithuanian`", inline=True)

        d7 = discord.Embed(color=0x00ff00)

        d7.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d7.set_thumbnail(url=self.lang_thumbnail)
        d7.set_image(url=self.lang_image)

        d7.add_field(name="🔺 lb",
                     value="`luxembourgish`", inline=True)
        d7.add_field(name="🔺 mk",
                     value="`macedonian`", inline=True)
        d7.add_field(name="🔺 mg",
                     value="`malagasy`", inline=True)
        d7.add_field(name="🔺 ms",
                     value="`malay`", inline=True)
        d7.add_field(name="🔺 ml",
                     value="`malayalam`", inline=True)
        d7.add_field(name="🔺 mt",
                     value="`maltese`", inline=True)
        d7.add_field(name="🔺 mi",
                     value="`maori`", inline=True)
        d7.add_field(name="🔺 mr",
                     value="`marathi`", inline=True)
        d7.add_field(name="🔺 mn",
                     value="`mongolian`", inline=True)
        d7.add_field(name="🔺 my",
                     value="`myanmar` (burmese)", inline=True)

        d8 = discord.Embed(color=0x00ff00)

        d8.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d8.set_thumbnail(url=self.lang_thumbnail)
        d8.set_image(url=self.lang_image)

        d8.add_field(name="🔺 ne",
                     value="`nepali`", inline=True)
        d8.add_field(name="🔺 no",
                     value="`norwegian`", inline=True)
        d8.add_field(name="🔺 or",
                     value="`odia`", inline=True)
        d8.add_field(name="🔺 ps",
                     value="`pashto`", inline=True)
        d8.add_field(name="🔺 fa",
                     value="`persian`", inline=True)
        d8.add_field(name="🔺 pl",
                     value="`polish`", inline=True)
        d8.add_field(name="🔺 pt",
                     value="`portuguese`", inline=True)
        d8.add_field(name="🔺 pa",
                     value="`punjabi`", inline=True)
        d8.add_field(name="🔺 ro",
                     value="`romanian`", inline=True)
        d8.add_field(name="🔺 ru",
                     value="`russian`", inline=True)

        d9 = discord.Embed(color=0x00ff00)

        d9.set_author(name="Language abbreviations",
                      icon_url=self.lang_icon_url)
        d9.set_thumbnail(url=self.lang_thumbnail)
        d9.set_image(url=self.lang_image)

        d9.add_field(name="🔺 sm",
                     value="`samoan`", inline=True)
        d9.add_field(name="🔺 gd",
                     value="`scots gaelic`", inline=True)
        d9.add_field(name="🔺 sr",
                     value="`serbian`", inline=True)
        d9.add_field(name="🔺 st",
                     value="`sesotho`", inline=True)
        d9.add_field(name="🔺 sn",
                     value="`shona`", inline=True)
        d9.add_field(name="🔺 sd",
                     value="`sindhi`", inline=True)
        d9.add_field(name="🔺 si",
                     value="`sinhala`", inline=True)
        d9.add_field(name="🔺 sk",
                     value="`slovak`", inline=True)
        d9.add_field(name="🔺 sl",
                     value="`slovenian`", inline=True)
        d9.add_field(name="🔺 so",
                     value="`somali`", inline=True)

        d10 = discord.Embed(color=0x00ff00)

        d10.set_author(name="Language abbreviations",
                       icon_url=self.lang_icon_url)
        d10.set_thumbnail(url=self.lang_thumbnail)
        d10.set_image(url=self.lang_image)

        d10.add_field(name="🔺 es",
                      value="`spanish`", inline=True)
        d10.add_field(name="🔺 su",
                      value="`sundanese`", inline=True)
        d10.add_field(name="🔺 sw",
                      value="`swahili`", inline=True)
        d10.add_field(name="🔺 sv",
                      value="`swedish`", inline=True)
        d10.add_field(name="🔺 tg",
                      value="`tajik`", inline=True)
        d10.add_field(name="🔺 ta",
                      value="`tamil`", inline=True)
        d10.add_field(name="🔺 te",
                      value="`telugu`", inline=True)
        d10.add_field(name="🔺 th",
                      value="`thai`", inline=True)
        d10.add_field(name="🔺 tr",
                      value="`turkish`", inline=True)
        d10.add_field(name="🔺 uk",
                      value="`ukrainian`", inline=True)

        d11 = discord.Embed(color=0x00ff00)

        d11.set_author(name="Language abbreviations",
                       icon_url=self.lang_icon_url)
        d11.set_thumbnail(url=self.lang_thumbnail)
        d11.set_image(url=self.lang_image)

        d11.add_field(name="🔺 ur",
                      value="`urdu`", inline=True)
        d11.add_field(name="🔺 ug",
                      value="`uyghur`", inline=True)
        d11.add_field(name="🔺 uz",
                      value="`uzbek`", inline=True)
        d11.add_field(name="🔺 vi",
                      value="`vietnamese`", inline=True)
        d11.add_field(name="🔺 cy",
                      value="`welsh`", inline=True)
        d11.add_field(name="🔺 xh",
                      value="`xhosa`", inline=True)
        d11.add_field(name="🔺 yi",
                      value="`yiddish`", inline=True)
        d11.add_field(name="🔺 yo",
                      value="`yoruba`", inline=True)
        d11.add_field(name="🔺 zu",
                      value="`zulu`", inline=True)

        embeds = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11]

        await paginator.Simple(
            PreviousButton=discord.ui.Button(
                label="<", style=discord.ButtonStyle.green),
            NextButton=discord.ui.Button(
                label=">", style=discord.ButtonStyle.green),
            FirstButton=discord.ui.Button(
                label="<<", style=discord.ButtonStyle.green),
            LastButton=discord.ui.Button(
                label=">>", style=discord.ButtonStyle.green),
            PageCounterStyle=discord.ButtonStyle.green,
            InitialPage=0,
            timeout=42069).start(ctx, pages=embeds)


async def setup(bot):
    await bot.add_cog(Dict(bot))
