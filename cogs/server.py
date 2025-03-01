import discord
from discord.ext import commands
from discord import app_commands
import traceback
import locale


class Server(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def server(self, ctx):

        locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

        cal = ctx.guild.created_at.strftime("%d %B %Y %A %H:%M:%S")

        embed = discord.Embed(color=0xc20000)
        embed.set_thumbnail(
            url=ctx.guild.icon)
        embed.set_author(
            name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.add_field(name='🆔 **Server ID:**',
                        value=f"> ```{ctx.guild.id}```", inline=False)
        embed.add_field(name="📅 **Server creation date:**",
                        value=f"> ```{cal}```", inline=False)
        embed.add_field(
            name='**Server owner**', value=f"> {ctx.guild.owner.mention}", inline=False)
        embed.add_field(name='**Member count:**',
                        value=f'> ```{ctx.guild.member_count}```', inline=False)
        embed.add_field(name='**Role count:**',
                        value=f'> ```{len(ctx.guild.roles) - 1}```', inline=False)
        embed.add_field(
            name='**Text channel count:**', value=f'> ```{len(ctx.guild.text_channels)}```', inline=False)
        embed.add_field(
            name='**Voice channel count:**', value=f'> ```{len(ctx.guild.voice_channels)}```', inline=False)
        await ctx.send(embed=embed)

    @app_commands.command(name="server-info", description="Server information")
    async def server_slash(self, interaction: discord.Interaction):

        try:
            locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

            cal = interaction.guild.created_at.strftime("%d %B %Y %A %H:%M:%S")

            embed = discord.Embed(color=0xc20000)
            embed.set_thumbnail(
                url=interaction.guild.icon)
            embed.set_author(
                name=interaction.guild.name, icon_url=interaction.guild.icon)
            embed.add_field(name='🆔 **Server ID:**',
                            value=f"> ```{interaction.guild.id}```", inline=False)
            embed.add_field(name="📅 **Server creation date:**",
                            value=f"> ```{cal}```", inline=False)
            embed.add_field(
                name='**Server owner**', value=f"> {interaction.guild.owner.mention}", inline=False)
            embed.add_field(name='**Member count:**',
                            value=f'> ```{interaction.guild.member_count}```', inline=False)
            embed.add_field(name='**Role count:**',
                            value=f'> ```{len(interaction.guild.roles) - 1}```', inline=False)
            embed.add_field(
                name='**Text channel count:**', value=f'> ```{len(interaction.guild.text_channels)}```', inline=False)
            embed.add_field(
                name='**Voice channel count:**', value=f'> ```{len(interaction.guild.voice_channels)}```', inline=False)
            await interaction.response.send_message(embed=embed)
        except:
            err = traceback.format_exc()
            await interaction.response.send_message(f"```py\n{err}```")


async def setup(bot: commands.Bot):
    await bot.add_cog(Server(bot))
