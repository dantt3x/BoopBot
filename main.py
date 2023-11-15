if __name__ == "__main__":
    from test import a_test_function
    print("init")
    a_test_function()

@boopbot.bot.event
async def on_ready():
    print("BoopBot is ready to run.")
    print("------------------------")

@boopbot.bot.event
async def on_message(message):  
    
    if message.author.bot:
        return
    if check_for_keywords(message) == 1:
        return
    await bot.process_commands(message)

bot.run('MTE3NDA3MTE3NDMwMTQ5MTMxMA.GmmgAa.lpEwcfOu2bazwuRCkpWZ0LbLYiIE5gtulc6PAw')