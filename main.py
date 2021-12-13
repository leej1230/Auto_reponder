import discord
#from discord_slash import SlashCommand
from discord.ext import commands
import random

Token = 'OTE5NzE1NzMyMjQ4NDc3NzE4.YbZ2Bg.TruM8zVEAjLtGDp11AXYG2_fNPQ'
#Add BOT's Token

client = commands.Bot(command_prefix="/")
#slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

'''
@client.command(name="Ping", description="Fuck no") #description="Shows the bots latency"
async def ping(ctx):
    await ctx.message.channel.send('npnp lol')

@client.command(name='Another', description='Why is it not working')
async def ano(ctx):
    ctx.message.channel.send('yeo')
'''
@client.event
async def on_message(message):
#message in parenthesis is every single message that goes into server
    username = str(message.author).split('#')[0]
    #message.author -> gets userID, i.e) test#1234
    #str(message.author).split('#') -> [test, 1234]
    user_message = str(message.content)
    channel = str(message.channel.name)
    #print(f'{username}: {user_message} ({channel})')
    #f in print -> replace the curly brackets variables {}

    #Bot COULD respond to itself
    #if message.author == client.user:
        #return

    #TO specify text channel: if message.channel.name == 'test':
    if user_message.lower() == 'hello':
        await message.channel.send(f'Hi again {username}!')
        return
    elif user_message.lower() == 'bye':
        await message.channel.send(f'Good bye {username}!')
        return
    elif user_message.lower() == '!random':
        response = f'This is your random number: {random.randrange(100000)}'
        await message.channel.send(response)
        return


client.run(Token)