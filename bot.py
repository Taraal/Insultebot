import os
import random
import discord

TOKEN = "Votre token discord"

client = discord.Client()

def create_insult():
    first_row = ["Espèce de ", "Sale ", "Enfoiré de ", "Batard de ", " Vil "]
    second_row = ["nazi ", "con ", "débile ", "gauchiste ", "droitard ", "journalope "]
    third_row = ["de merde", "à la con", "trépané", "lobotomisé", "à poils longs"]
    return random.choice(first_row) + random.choice(second_row) + random.choice(third_row)

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!insulte'):
        if len(message.mentions) > 0:
            for user in message.mentions:
                insulte = create_insult()
                msg = f'<@{user.id}> {insulte}'.format(message)
                await message.channel.send(msg)

@client.event
async def on_ready():
    print('Connecté')
    print('------')

client.run(TOKEN)