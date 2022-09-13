import json
import os
import random

from dotenv import load_dotenv
import discord

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def create_insult():
    
    data = json.load(open('insultes.json', "rb"))

    return random.choice(data['first_row']) + random.choice(data['second_row']) + random.choice(data['third_row'])

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!insulte'):
        if len(message.mentions) > 0:
            try: 
                for user in message.mentions:
                    insulte = create_insult()

                    msg = f'<@{user.id}> {insulte}'.format(message)

                    await message.channel.send(msg)
            except Exception:
                print(Exception)

@client.event
async def on_ready():
    print('Connecté')
    print('------')

client.run(TOKEN)