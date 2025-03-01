import discord
from discord.ext import commands
from discord import app_commands
import traceback


class UnlockChannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_admin(self, user):
        return user.guild_permissions.change_nickname

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def unlocked(self, ctx):
        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f"{channel.mention} has unlocked.")

    @app_commands.command(name="unlock", description="Unlocks a channel")
    async def unlock_slash(self, interaction: discord.Interaction):
        try:
            if self.is_admin(interaction.user):
                channel = interaction.channel
                overwrite = channel.overwrites_for(
                    interaction.guild.default_role)
                overwrite.send_messages = True
                await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
                await interaction.response.send_message(f"{channel.mention} has unlocked.")
        except:
            err = traceback.format_exc()
            await interaction.response.send_message(f"```py\n{err}```")


async def setup(bot: commands.Bot):
    await bot.add_cog(UnlockChannel(bot))
