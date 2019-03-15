import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
from random import *
import os
from discord.utils import get

client = commands.Bot(command_prefix = "-!")
client.remove_command('help')
status = ['Rocky', 'x', 'Rachel']
jessie = 0

@client.command()
async def ping():
    await client.say('Pong!')


@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        color = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='**-ping**', value='Returns Pong!', inline=False)
    
    embed.add_field(name='**-say <string>**', value='Tells the bot to say something.', inline=False)
    

    await client.say(embed=embed) #send_message(author, embed=embed)


@client.command()
async def jessiegay():
    await client.say("Jessie has said gay %d times" % jessie)



@client.command()
async def say(*args):
    output = ' '
    for word in args:
        output += word
        output += ' '
    await client.say(output)
    
    
    

client.run(os.environ['BOT_TOKEN'])    
