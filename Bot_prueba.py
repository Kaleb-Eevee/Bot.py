import discord
from Bot_logic import gen_pass
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix = "!", intents = intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send("😭👍")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def Iloveyou(ctx):
    await ctx.send("Yo también te quiero 😍")

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} se ha unido el {discord.utils.format_dt(member.joined_at)} ¡es bueno tenerte aquí desde hace tiempo!')

@bot.command()
async def Voidmeme(ctx):
    await ctx.send("Eso es muy void de tu parte 👀")

bot.run("MTI3NTk3ODU5MjkzMjg2MDA3OA.Gg2F-0.9KxrIVsmIwldVIIWqhUMdVPxw7gqV7Vm_mENis")
