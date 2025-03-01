import discord
from discord.ext import commands
import re
from alf import *


def replace_letters(args, letters):
    replaced_text = ""
    for char in args:
        if char in letters:
            replaced_text += letters[char]
        else:
            replaced_text += char
    return replaced_text


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def giverole(self, ctx, member: commands.Greedy[discord.Member], *, role_name: str):
        try:
            pattern = re.compile(
                r"^(?!.*<a?:\w+:\d+>)[a-zA-Z0-9ğüşıöçĞÜŞİÖÇ ]+$|^(?!.*<a?:\w+:\d+>)\|[a-zA-Z0-9ğüşıöçĞÜŞİÖÇ ]+$|^[a-zA-Z0-9ğüşıöçĞÜŞİÖÇ ]+$")
            if not pattern.match(role_name):
                await ctx.send("```Role name can only contain letters and numbers.```")
                return
            roles = sorted(ctx.guild.roles,
                           key=lambda r: r.name.lower(), reverse=False)
            embed = discord.Embed(colour=0x00ff00)
            target_roles = [role_name]
            for role in roles:
                if role.name in target_roles and role_name.lower() == role.name.lower():
                    for i in member:
                        await i.add_roles(role)
                        embed.description = f"{i.mention} **<@&{role.id}> is given.**"
                    await ctx.send(embed=embed)
                    break
                elif re.search(fr"\b{re.escape(role_name)}\w*\b", role.name, re.IGNORECASE):
                    for i in member:
                        await i.add_roles(role)
                        embed.description = f"{i.mention} **<@&{role.id}> is given.**"
                    await ctx.send(embed=embed)
                    break
            else:
                await ctx.send(f"**__{role_name}__** does not exist.")
        except discord.Forbidden:
            embed = discord.Embed(colour=0xff0000)
            embed.add_field(name="__**The reasons for the error could be one or more of the following.:**__", value=f"""
            > I do not have sufficient permissions for this action.
            > (<@{self.bot.user.id}>)
            > <@{ctx.author.id}> You do not have sufficient permissions for this action.
            > The role you are trying to assign is the bot's integration role ***(the role with the bot's name, which is automatically created when the bot joins the server)***.
            > 
            > ```You can resolve your error by checking the above-mentioned points.```
            """, inline=False)
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("```An error occurred while assigning the role.```")

    @commands.command()
    @commands.has_permissions(change_nickname=True)
    async def takerole(self, ctx, member: commands.Greedy[discord.Member], *, role_name: str):
        try:
            pattern = re.compile(
                r"^(?!.*<a?:\w+:\d+>)[a-zA-Z0-9ğüşıöçĞÜŞİÖÇ ]+$|^(?!.*<a?:\w+:\d+>)\|[a-zA-Z0-9ğüşıöçĞÜŞİÖÇ ]+$|^[a-zA-Z0-9ğüşıöçĞÜŞİÖÇ ]+$")
            if not pattern.match(role_name):
                await ctx.send("```Role name can only contain letters and numbers.```")
                return
            roles = sorted(ctx.guild.roles,
                           key=lambda r: r.name.lower(), reverse=False)
            embed = discord.Embed(colour=0xff0000)
            target_roles = [role_name]
            for role in roles:
                if role.name in target_roles and role_name.lower() == role.name.lower():
                    for i in member:
                        await i.remove_roles(role)
                        embed.description = f"{i.mention} **<@&{role.id}> has taken.**"
                    await ctx.send(embed=embed)
                    break
                elif re.search(fr"\b{re.escape(role_name)}\w*\b", role.name, re.IGNORECASE):
                    for i in member:
                        await i.remove_roles(role)
                        embed.description = f"{i.mention} **<@&{role.id}> has taken.**"
                    await ctx.send(embed=embed)
                    break
            else:
                await ctx.send(f"**__{role_name}__** does not exist.")
        except discord.Forbidden:
            embed = discord.Embed(colour=0xff0000)
            embed.add_field(name="__**The reasons for the error could be one or more of the following.:**__", value=f"""
            > I do not have sufficient permissions for this action.
            > (<@{self.bot.user.id}>)
            > <@{ctx.author.id}> You do not have sufficient permissions for this action.
            > The role you are trying to assign is the bot's integration role ***(the role with the bot's name, which is automatically created when the bot joins the server)***.
            > 
            > ```You can resolve your error by checking the above-mentioned points.```
            """, inline=False)
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("```An error occurred while assigning the role.```")


async def setup(bot):
    await bot.add_cog(Roles(bot))
