import discord
from discord.ext import commands



description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author== bot.user:
        return
    if "puta" in message.content.lower():
       await message.channel.send(f"No seas grocero en este canal {message.author.name}")

    await bot.process_commands(message)


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

bot.run('MTI4OTYyODI1MzY3MzM1NzM1Mw.GkzSJz.xhju317CY4JxcjWn_qNwsXNFgEs6s7osWqbWnI')