import discord
from discord.ext import commands
from discord import app_commands
import traceback
from typing import Optional


class UserInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, member: Optional[discord.Member]):
        if not member:
            member = ctx.author

        roles = [role for role in member.roles]
        embed = discord.Embed(colour=0x00ff00)
        embed.set_thumbnail(url=member.avatar)
        embed.add_field(
            name="`ID:`", value=f"> ```{member.id}```", inline=False)
        embed.add_field(name="`User name` ",
                        value=f"> ```{member.name}```", inline=False)
        embed.add_field(name="`Server name` ",
                        value=f"> ```{member.display_name}```", inline=False)
        embed.add_field(name="`Account creation date:`", value="> "+member.created_at.strftime(
            "```%a, %#d %B %Y, %I:%M %p UTC```"), inline=False)
        embed.add_field(name="`Server join date:`", value="> "+member.joined_at.strftime(
            "```%a, %#d %B %Y, %I:%M %p UTC```"), inline=False)
        embed.add_field(name=f"`The roles owned` ({len(roles)})", value="> "+" ".join(
            [role.mention for role in roles]), inline=False)
        embed.add_field(name="`Top role:`",
                        value="> "+member.top_role.mention, inline=False)
        await ctx.send(embed=embed)

    @app_commands.command(name="user-info", description="Display user information.")
    async def userinfo_slash(self, interaction: discord.Interaction, member: Optional[discord.Member]):
        try:
            if not member:
                member = interaction.user

            roles = [role for role in member.roles]
            embed = discord.Embed(colour=0x00ff00)
            embed.set_thumbnail(url=member.avatar)
            embed.add_field(
                name="`ID:`", value=f"> ```{member.id}```", inline=False)
            embed.add_field(name="`User name` ",
                            value=f"> ```{member.name}```", inline=False)
            embed.add_field(name="`Server name` ",
                            value=f"> ```{member.display_name}```", inline=False)
            embed.add_field(name="`Account creation date:`", value="> "+member.created_at.strftime(
                "```%a, %#d %B %Y, %I:%M %p UTC```"), inline=False)
            embed.add_field(name="`Server join date:`", value="> "+member.joined_at.strftime(
                "```%a, %#d %B %Y, %I:%M %p UTC```"), inline=False)
            embed.add_field(name=f"`The roles owned` ({len(roles)})", value="> "+" ".join(
                [role.mention for role in roles]), inline=False)
            embed.add_field(name="`Top role:`",
                            value="> "+member.top_role.mention, inline=False)
            await interaction.response.send_message(embed=embed)

        except:
            err = traceback.format_exc()
            await interaction.response.send_message(f"```py\n{err}```")


async def setup(bot: commands.Bot):
    await bot.add_cog(UserInfo(bot))
