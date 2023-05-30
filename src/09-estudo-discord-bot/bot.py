from decouple import config
from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready():
    print(f"Pronto e conectado como {bot.user}")
    await load_cogs(bot)
    await bot.get_cog('Dates').current_time.start()
    
async def load_cogs(bot):
    for file in os.listdir("src/09-estudo-discord-bot/commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f"commands.{cog}")
    await bot.load_extension("tasks.dates")
    await bot.load_extension("manager")

TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)