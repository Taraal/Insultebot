import os
import random
import discord

TOKEN = "Votre token Discord"

client = discord.Client()

def create_insult():
    first_row = ["Espèce de ", "Sale ", "Enfoiré de ", "Batard de ", " Vil ", "Putain de ", "Bordel de ", "Enculé de ", "Tête de ", "Salaud de ", "Foutu ", "Fichu ", "Satané ", "Diable de "]
    second_row = ["nazi ", "con ", "débile ", "gauchiste ", "droitard ", "journalope ", "branleur ", "bouffon ", "casse-burnes ", "fripouille ", "fachiste ", "gland ", "garce ", "chieur ", "bite ", "boulet ", "connard ", "islamo-gauchiste ", "petite bite ", "pignouf ", "lopette ", "mange-merde ", "merdeux ", "minus ", "morue ", "moins-que-rien ", "naze ", "petite merde ", "porc ", "pute ", "raclure ", "résidu de capote ", "raclure de bidet ", "raté ", "sac à foutre ", "sac à merde ", "salope ", "sans-couilles ", "sent-la-pisse ", "teubé ", "tôcard ", "truie ", "trouduc ", "zgeg ", "vaurien "]   
    third_row = ["de merde", "à la con", "trépané", "lobotomisé", "à poils longs", "vulgaire ", "de ses morts ", "de droite ", "de gauche ", "de ta race"]
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