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

@bot.command()
async def prog_meme(ctx):
    with open("memes/mem1.jpg", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def ran_p_meme(ctx):
    mem_alet = random.choice(os.listdir("memes"))

    with open(f"memes/{mem_alet}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("EL TOKEN DEBE IR AQUI")
