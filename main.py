import config
import keywords
import commands

if __name__ == "__main__":
    config.initialize()


@config.bot.event
async def on_ready():
    print("BoopBot is ready to run.")
    print("------------------------")
    await config.bot.add_cog(commands.Liberal(config.bot))

@config.bot.event
async def on_message(message):  
    
    if message.author.bot:
        return
   
    await keywords.check_for_keywords(message)
    await config.bot.process_commands(message)

config.bot.run('MTE3NDA3MTE3NDMwMTQ5MTMxMA.GmmgAa.lpEwcfOu2bazwuRCkpWZ0LbLYiIE5gtulc6PAw')