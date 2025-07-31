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


async def response(
    message: discord.Message,
    text: str,
    response: str,
    allow_prefix: bool = True,
    allow_suffix: bool = True,
    allow_mention: bool = True,
):
    if allow_prefix:
        if message.content.lower().startswith(f"@gork {text}"):
            await message.reply(response)
            return
        if allow_mention and message.content.lower().startswith(
            f"{bot.user.mention} {text}"
        ):
            await message.reply(response)
            return
    if allow_suffix:
        if message.content.lower().startswith(f"{text} @gork"):
            await message.reply(response)
            return
        if allow_mention and message.content.lower().startswith(
            f"{text} {bot.user.mention}"
        ):
            await message.reply(response)
            return


@bot.event
async def on_message(message: discord.Message):
    await response(message, "is this real", "idk you figure it out")
    await response(message, "are you real", "yeh")

    await bot.process_commands(message)


bot.run(config.DISCORD_TOKEN)
