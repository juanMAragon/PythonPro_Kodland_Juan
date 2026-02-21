import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


lista_dati_curiosi = ["dato1...", "dato2...", ]

RIFIUTI = {
    "cartone del latte": "carta",
    "bottiglia di plastica": "plastica",
    "flacone di detersivo": "plastica",
    "barattolo di vetro": "vetro",
    "lattina": "plastica e metalli",
    "scatola di cartone": "carta",
    "fazzoletti usati": "organico",
    "avanzi di cibo": "organico",
    "pellicola trasparente": "indifferenziato",
    "scontrino": "indifferenziato"
}

@bot.command()
async def dove(ctx, *, oggetto: str):
    oggetto = oggetto.lower()

    if oggetto in RIFIUTI:
        bidone = RIFIUTI[oggetto]
        await ctx.send(f"{oggetto} → va nel bidone: {bidone}")
    else:
        await ctx.send("Oggetto non trovato nel database.")

bot.run("")