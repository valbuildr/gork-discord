import discord
from discord.ext import commands
import random
import config

bot = commands.Bot(
    command_prefix="g.", intents=discord.Intents(message_content=True, messages=True)
)

bot.remove_command("help")  # gork needs no help


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.change_presence(
        activity=discord.Activity(
            name="your deepest secrets", type=discord.ActivityType.listening
        )
    )


@bot.command(name="sync", hidden=True)
@commands.is_owner()
async def sync(ctx: commands.Context):
    m = await ctx.send(content="🔵 Syncing...")
    try:
        await bot.tree.sync()
        await m.edit(content="🟢 Application commands successfully synced!")
    except:
        await m.edit(content="🔴 An error occurred.")


@bot.event
async def on_message(message: discord.Message):
    if (
        message.content.lower().startswith(f"{bot.user.mention} is this real")
        or message.content.lower().startswith("@gork is this real")
        or message.content.lower().startswith(f"is this real {bot.user.mention}")
        or message.content.lower().startswith(f"is this real @gork")
    ):
        c = random.randint(0, 99)
        if c == 99:
            await message.reply("probably")
        else:
            await message.reply("idk you figure it out")
    elif (
        message.content.lower().startswith(f"{bot.user.mention} are you real")
        or message.content.lower().startswith(f"@gork are you real")
        or message.content.lower().startswith(f"are you real {bot.user.mention}")
        or message.content.lower().startswith(f"are you real @gork")
    ):
        await message.reply("yeh")

    await bot.process_commands(message)


bot.run(config.DISCORD_TOKEN)
