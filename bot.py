import json
import os
import random

from dotenv import load_dotenv
import discord
from discord import app_commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

class Bot(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        await self.tree.sync()    


intents = discord.Intents.default()
client = Bot(intents=intents)

def create_insult():
    data = json.load(open('insultes.json', "rb"))
    return random.choice(data['first_row']) + random.choice(data['second_row']) + random.choice(data['third_row'])

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def insulte(interaction: discord.Interaction, member : discord.Member):

    try:
        insulte = create_insult()

        msg = f'{member.mention} {insulte}'.format()

        await interaction.response.send_message(msg)

    except Exception as e:
        print(e)


client.run(TOKEN)
