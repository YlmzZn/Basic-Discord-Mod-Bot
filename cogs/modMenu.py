# Sadece sunucudaki yetkililer için komut menüsü.
import discord
from discord.ext import commands
import paginator


class ModMenu(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def mod(self, ctx):

        thumb = "image url"
        img = "image url"

        embed = discord.Embed(color=0xc20000)

        embed.set_thumbnail(url=thumb)
        embed.set_image(url=img)

        embed.add_field(name="**Give role**:",
                        value="> ```.giverole + <@user> + {role name}```", inline=False)
        embed.add_field(name="**Take role**:",
                        value="> ```.takerole + <@user> + {role name}```", inline=False)
        embed.add_field(name="**Fancy text font**:",
                        value="> ```.r + {sentence}```", inline=False)

        embed1 = discord.Embed(color=0xc20000)

        embed1.set_thumbnail(url=thumb)
        embed1.set_image(url=img)

        embed1.add_field(name="**Kick:**",
                         value="> ```.kick + <@user>```", inline=False)
        embed1.add_field(name="**Ban:**",
                         value="> ```.ban + <@user>```", inline=False)
        embed1.add_field(name="**Unban:**",
                         value="> ```.unban + <@user>```", inline=False)
        embed1.add_field(name="**🤐 Mute:**",
                         value="> ```.mute + <@user>```", inline=False)
        embed1.add_field(name="**😁 Unmute:**",
                         value="> ```.unmute + <@user>```", inline=False)

        embed2 = discord.Embed(color=0xc20000)

        embed2.set_thumbnail(url=thumb)
        embed2.set_image(url=img)

        embed2.add_field(name="**🧹 Clear chat:**",
                         value="> ```.cls + <@user> + <amount>```\n> • ***(tagging the user is optional.)***\n> • *Only the messages of the mentioned person are deleted.*", inline=False)
        embed2.add_field(name="**🔑 Lock channel**:",
                         value="> ```.locked```", inline=False)
        embed2.add_field(name="**🔐 Unlock channel**:",
                         value="> ```.unlocked```", inline=False)

        embed3 = discord.Embed(color=0xc20000)

        embed3.set_thumbnail(url=thumb)
        embed3.set_image(url=img)

        embed3.add_field(name="**Make an existing channel __hidden__ mode.**:",
                         value="> ```.pth + {channel name}```", inline=False)
        embed3.add_field(name="**Make an existing hidden channel __public__ mode.**:",
                         value="> ```.htp + {channel name}```", inline=False)
        embed3.add_field(name="**Create a hidden text channel.**:",
                         value="> ```.htc + {new channel name}```", inline=False)
        embed3.add_field(name="**Create a hidden voice channel.**:",
                         value="> ```.hvc + {new channel name}```", inline=False)

        embed4 = discord.Embed(color=0xc20000)

        embed4.set_thumbnail(url=thumb)
        embed4.set_image(url=img)

        embed4.add_field(name="**➕ Add new auto responder**:",
                         value='> ```.add + "{message}" + "{answer}"```', inline=False)
        embed4.add_field(name="**👁️ View all auto-responder messages.**:",
                         value='> ```/messages```', inline=False)
        embed4.add_field(name="**📛 Delete a specific auto-responder.**:",
                         value='> ```.delete + {message number}```', inline=False)
        embed4.add_field(name="**Delete all auto-responder.**:",
                         value='> ```.reset```', inline=False)

        embeds = [embed, embed1, embed2, embed3, embed4]

        await paginator.Simple(
            PreviousButton=discord.ui.Button(
                label="<", style=discord.ButtonStyle.grey),
            NextButton=discord.ui.Button(
                label=">", style=discord.ButtonStyle.grey),
            FirstButton=discord.ui.Button(
                label="<<", style=discord.ButtonStyle.grey),
            LastButton=discord.ui.Button(
                label=">>", style=discord.ButtonStyle.grey),
            PageCounterStyle=discord.ButtonStyle.grey,
            InitialPage=0,
            timeout=42069).start(ctx, pages=embeds)


async def setup(bot: commands.Bot):
    await bot.add_cog(ModMenu(bot))
