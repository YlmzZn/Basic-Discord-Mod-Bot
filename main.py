import discord
from discord.ext import commands, tasks
import DiscordUtils
import random
import os
import json
import asyncio
from pages import Pagination

with open("config.json", "r") as config_file:
    config = json.load(config_file)

BOT_TOKEN = config["BOT_TOKEN"]
PREFIX = config["PREFIX"]

intents = discord.Intents.all()  # Intent permissions

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

bot.remove_command('help')  # Remove default help command

tracker = DiscordUtils.InviteTracker(bot)

states = ["state1", "state2"]  # Bot's state.


# Every 5 seconds, the bot's status is randomly selected from the 'states' variable.
@tasks.loop(seconds=5.0)
async def my_background_task():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(states)))


@bot.event
async def on_ready():
    print('•••Ready•••')

    try:
        synced = await bot.tree.sync()  # Synchronizes slash commands
        print(f"○○○Synced {len(synced)} command(s)○○○")
    except Exception as e:
        print(e)

    await tracker.cache_invites()
    await bot.wait_until_ready()
    my_background_task.start()
    await update_member_count_loop()

# The ID of the channel where you want the current member count to be displayed.
CHANNEL_ID = 12160038472

SERVER_ID = 64373972784  # Server ID.


async def update_member_count_loop():  # Keeps the member count up to date.
    await bot.wait_until_ready()

    guild = bot.get_guild(SERVER_ID)

    channel = bot.get_channel(CHANNEL_ID)

    while not bot.is_closed():
        await update_member_count(guild, channel)

        # An update is made every 10 minutes. (Recommended interval: 10 minutes.)
        await asyncio.sleep(600)


# Channel which displaying the member count.
async def update_member_count(guild, channel):
    member_count = guild.member_count
    await channel.edit(name=f'📍・{member_count} members')


@bot.event
# It is triggered when the user creates a server invite.
async def on_invite_create(invite):
    await tracker.update_invite_cache(invite)


@bot.event
# It identifies the member who joined the server.
async def on_guild_join(guild):
    await tracker.update_guild_cache(guild)


@bot.event
# It is triggered when the invite created by the user is deleted.
async def on_invite_delete(invite):
    await tracker.remove_invite_cache(invite)


@bot.event
# It identifies the user who left the server.
async def on_guild_remove(guild):
    await tracker.remove_guild_cache(guild)


@bot.event
# It is triggered when a member joins the server.
async def on_member_join(member: discord.Asset):

    if member.guild.id == SERVER_ID:

        channel_id = "7054230437"  # Channel ID for the welcome message.
        # The role to be given to the person who joins the server.
        role_id = "705440607199"

        inviter = await tracker.fetch_inviter(member)

        welcome_channel = bot.get_channel(
            channel_id)

        give_member_role = discord.utils.get(
            member.guild.roles, id=role_id)

        await welcome_channel.send(member.mention)

        try:
            # Welcome message.
            j1 = discord.Embed(
                description=f"## Welcome {member.mention}\n\n> ### Member count: **`# {member.guild.member_count}`**\n> ### Invite: <@{inviter.id}>", color=0xc20000)
        except:
            # The situation where the invite cannot be determined.
            j1 = discord.Embed(
                description=f"## Welcome {member.mention}\n\n> ### Member count: **`# {member.guild.member_count}`**\n> ### Invite: **`Bilinmiyor`**", color=0xc20000)

        if member.avatar:
            j1.set_thumbnail(url=member.avatar)
        else:
            # Avatar does not exist.
            j1.set_thumbnail(
                url="")

        await welcome_channel.send(embed=j1)

        await member.add_roles(give_member_role)

        dm = await member.create_dm()  # Send message via DM.

        await dm.send("")


@bot.command()  # For voice channel. (for bot.)
@commands.has_permissions(change_nickname=True)
async def join(ctx):
    await ctx.author.voice.channel.connect()


@bot.command()  # Auto responder.
@commands.has_permissions(change_nickname=True)
async def add(ctx, mesaj, cevap):

    djson = {}

    try:
        with open('json/authoresponder.json', 'r', encoding='utf-8') as file:
            djson = json.load(file)
    except FileNotFoundError:
        djson = []

    mesaj = mesaj.replace("\\n", "\n")
    cevap = cevap.replace("\\n", "\n")

    djson.append({
        "interaction_id": str(ctx.author.name),
        "message": mesaj,
        "answer": cevap,
    })

    try:
        with open(f'json/authoresponder.json', 'w', encoding="utf-8") as file:
            json.dump(djson, file, indent=4)
        await ctx.send("## Message created.")
    except:
        await ctx.send("```Error```")


@bot.tree.command(name="message", description="Auto responder setting")
@commands.has_permissions(change_nickname=True)
async def message(ctx: discord.Interaction):
    with open("json/authoresponder.json", "r", encoding="utf-8") as file:
        show = json.load(file)

    L = 5

    liste = []

    j = 1
    for entries in show:
        m = entries['message'].replace("\n", "\n> ")
        c = entries['answer'].replace("\n", "\n> ")
        a = f"`{j}) {entries['interaction_id']}`\n> ===`Message`===\n> {m}\n> ===`Answer`===\n> {c}"
        j += 1
        liste.append(a)

    async def get_page(page: int):
        emb = discord.Embed(color=0xc20000)
        offset = (page-1) * L
        for user in liste[offset:offset+L]:
            emb.description += f"{user}\n"
        n = Pagination.compute_total_pages(len(liste), L)
        emb.set_footer(text=f"{page}/{n}")
        return emb, n

    await Pagination(ctx, get_page).navegate()


@bot.command()  # Delete auto responder.
@commands.has_permissions(change_nickname=True)
async def sil(ctx, i: int):
    with open("json/authoresponder.json", "r", encoding="utf-8") as file:
        show = json.load(file)
    index = i - 1
    if index >= 0 and index <= len(show):
        del show[index]

        with open("json/authoresponder.json", "w", encoding="utf-8") as file:
            json.dump(show, file, indent=4, ensure_ascii=False)

        embed = discord.Embed(
            description=f"**Message number `{i}` was deleted..**", color=0xff0000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            description=f"** There is no message with such a number.**", color=0xFF9900)
        await ctx.send(embed=embed)


@bot.command()  # Delete all auto responder.
@commands.has_permissions(change_nickname=True)
async def sıfırla(ctx):
    with open("json/authoresponder.json", "r", encoding="utf-8") as file:
        show = json.load(file)

    show = []

    with open("json/authoresponder.json", "w", encoding="utf-8") as file:
        json.dump(show, file, indent=4, ensure_ascii=False)

    embed = discord.Embed(
        description=f"**All messages are deleted.**", color=0xff0000)
    await ctx.send(embed=embed)


@bot.event  # Tracks user messages.
async def on_message(message):

    if not message.author.bot:
        with open('json/authoresponder.json', 'r', encoding="utf-8") as file:
            authoresponder_data = json.load(file)

        for data_list in authoresponder_data:
            if message.content.lower().startswith(data_list["message"] + " "):
                await message.reply(data_list["answer"])
                break
            elif message.content.lower().startswith(data_list["message"]) and message.content.lower().endswith(data_list["message"]):
                await message.reply(data_list["answer"])
                break

    await bot.process_commands(message)


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(BOT_TOKEN)
asyncio.run(main())
