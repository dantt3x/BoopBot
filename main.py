import discord
from discord.ext import commands

botIntents = discord.Intents.all()
botIntents.members = True

bot = commands.Bot(command_prefix='$', intents=botIntents)

liberal_active = False

@bot.event
async def on_ready():
    print("BoopBot is ready to run.")
    print("------------------------")
    
@bot.command()
async def liberal_check(ctx):
    print("cmd")
    await ctx.send("all these CRAZYYY liberals... they continue to ruin this GREAT AMERICAN NATION! Are you a liberal?")
    global liberal_active
    liberal_active = True

@bot.event
async def on_message(message):  
    global liberal_active
    
    if message.author.bot:
        return
    
    contents = message.content.lower()
    
    
    if liberal_active == True:
        if contents == "yes":
            await message.channel.send("UNBELIEVABLE!!!!!!")
            liberal_active = False
        elif contents == "no":
            await message.channel.send("gooooooood!!!!!!")
            liberal_active = False

    if contents == "jacob":
        await message.channel.send("https://tenor.com/view/jacob-gif-1687100335585512029")
    if contents == "nick":
        await message.channel.send("https://media.discordapp.net/attachments/495286269459300364/1017645613971685506/2E2C5956-0C49-40AC-BDF7-C8FCCAC16E18.gif")
    if contents == "marcos" or contents == "marc":
        await message.channel.send("https://media.discordapp.net/attachments/1092111312529653933/1111734848483233943/attachment-3.gif")
    if contents == "joseph":
        await message.channel.send("https://media.discordapp.net/attachments/470168157148020756/1069459474840035398/RDT_20230129_1856533783651655226913782.gif")
        
        
    await bot.process_commands(message)
    

bot.run('MTE3NDA3MTE3NDMwMTQ5MTMxMA.GmmgAa.lpEwcfOu2bazwuRCkpWZ0LbLYiIE5gtulc6PAw')