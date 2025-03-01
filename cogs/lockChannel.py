import discord
from discord.ext import commands
from discord import app_commands
import traceback


class LockChannel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_admin(self, user):
        return user.guild_permissions.change_nickname

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def locked(self, ctx):
        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send(f"{channel.mention} has locked.")

    @app_commands.command(name="lock", description="Locks a channel.")
    async def lock_slash(self, interaction: discord.Interaction):
        try:
            if self.is_admin(interaction.user):
                channel = interaction.channel
                overwrite = channel.overwrites_for(
                    interaction.guild.default_role)
                overwrite.send_messages = False
                await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
                await interaction.response.send_message(f"{channel.mention} has locked.")
        except:
            err = traceback.format_exc()
            await interaction.response.send_message(f"```py\n{err}```")


async def setup(bot: commands.Bot):
    await bot.add_cog(LockChannel(bot))
