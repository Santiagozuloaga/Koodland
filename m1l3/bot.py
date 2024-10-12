import discord
from discord.ext import commands
import random


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@bot.event
async def on_message(message):
    if message.author== bot.user:
        return
    if "puta" in message.content.lower():
       await message.channel.send(f"No seas grocero en este canal {message.author.name}")

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
@bot.command()
async def sumar(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def restar(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def multiplicar(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def dividir(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)



@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.command()
async def info (ctx):
    await ctx.send ("Soy un bot programaddo por deimos")
@bot.command()
async def emoji (ctx):
    await ctx.send ("\U0001F600")
    
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



@bot.group()
async def cool(ctx):
      await ctx.send(f'{ctx.subcommand_passed} is cool')

bot.run('MTI4OTYyODI1MzY3MzM1NzM1Mw.GcHQ3t.zoRfm-pYB3UANyubbGTFi28qb8FrP8N8xPg6Qo')