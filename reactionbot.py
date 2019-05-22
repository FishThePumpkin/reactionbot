import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
from random import *
import os
from discord.utils import get

import lists
from lists import reactionsdict

client = commands.Bot(command_prefix = '-!')
client.remove_command('help')
status = ['Rocky', 'x', 'Rachel']

inmsg = {
    "wink": "lstwink",
    "baka": "lsttsun",
    "?": "lstquestion",
    "toxic": "lsttoxic",
    "<@547365819122712586>": "lstping",
    ":GWsocksBlobAngeryPing:": "lstdash",
    ":GWsocksThonkeryPing:": "lstdash",
    ":GWcmeisterPeepoShrug:": "lstdash",
    ":GWchadThink:": "lstdash",
    "123hearts": "lsthearts",
    "123emoji", "lstemoji",
    "123jessie", "lstjessie"
}
IDs = {
    "Jessie": "290419231734890497",
    "Vivian": "346924005997019139",
    "Owner": "246437474463776769",
    "Bot": "556089994708779033",
    "Rachel": "318366307169075201",
    "Labib": "378820414350295040",
    "Trung": "328345368494342155"
}


async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(2)
          
@client.event
async def on_message(message):
    author = message.author
    chance = randint(1,7)
    mess = message.content.lower()
    for i in inmsg:
        if i in mess:
            await get_reaction(message,i)
            
    if message.content == '?':
        await get_reaction(message,"?")
         
    elif author.id == IDs["Rachel"] or author.id == IDs["Trung"]:               #318366307169075201
        await get_reaction(message,"123hearts")
    
    elif author.id == IDs["Jessie"]:
        await get_reaction(message,"123jessie")
        await client.add_reaction(message,reactionsdict["lstgay"][0])
        await client.add_reaction(message,reactionsdict["lstgay"][1])
        await client.add_reaction(message,reactionsdict["lstgay"][2])
        await get_reaction(message,"123jessie")
    
    if chance == 2: 
        get_reaction(message,"123emoji")

async def get_reaction(message,i):
    index = randint(0,len(reactionsdict[inmsg[i]]) - 1)
    try:
       return await client.add_reaction(message,reactionsdict[inmsg[i]])
    except:
        if message.content.find('EMOJI_NAME'):
            for x in client.get_all_emojis():
                if x.id == reactionsdict[inmsg[i]][index]:
                    return await client.add_reaction(message, x)
        
        
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
async def say(*args):
    output = ' '
    for word in args:
        output += word
        output += ' '
    await client.say(output) 
    
client.loop.create_task(change_status())
client.run(os.environ['BOT_TOKEN'])    
