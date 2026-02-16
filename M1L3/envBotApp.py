import discord
import os
from dotenv import load_dotenv   # NEW

# carica il file .env
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")

    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")

    else:
        await message.channel.send(message.content)


TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN non trovato nel file .env")

client.run(TOKEN)
