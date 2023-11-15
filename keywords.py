import csv

async def check_for_keywords(message):
    content = message.content.lower()
    
    with open('keywords.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if content == row['name']:
                await message.channel.send(row['response'])
              