import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional


class Banner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="avatar", description="Display user avatar.")
    async def avatar_slash(self, interaction: discord.Interaction,
                           member: Optional[discord.Member]
                           ):
        try:
            if not member:
                member = interaction.user
            embed = discord.Embed(color=0x2f3136)
            embed.set_image(url=member.avatar)
            await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(f"### <@{member.id}> likely has the default Discord profile picture!", ephemeral=True)

    @app_commands.command(name="banner", description="Display user banner.")
    async def banner_slash(self, interaction: discord.Interaction,
                           member: Optional[discord.Member]
                           ):
        try:

            if not member:
                member = interaction.user
            user_banner = await self.bot.fetch_user(member.id)
            embed = discord.Embed(color=0x2f3136)
            embed.set_image(url=user_banner.banner)
            await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(f"## <@{member.id}> does not have a banner.", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Banner(bot))
