import discord
from discord.ext import commands


class Liberal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active = False
    
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author.bot:
            return
        
        print(self.active)
        
        if self.active == True:
            content = message.content.lower()  
            self.active = False
            print(self.active)
            
            if content == "yes":
                await message.channel.send("UNBELIEVABLE!!!!!")
            elif content == "no":
                await message.channel.send("goooooood!!!!")
                
        

    @commands.command()
    async def liberal(self, ctx):
        await ctx.send(f'STINKING LIBERALS!!!!! are YOUUU a liberal??????')
        self.active = True

    


    


    