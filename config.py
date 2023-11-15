import discord
from discord.ext import commands

bot = ""
intents = ""

def initialize():
    global bot
    global intents
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix="/",intents=intents)