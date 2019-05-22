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
from lists import inmsg
import permissions
from permissions import IDs

client = commands.Bot(command_prefix = '-!')
client.remove_command('help')
status = ['Rocky', 'x', 'Rachel']

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
    
    if chance == 2: 
        return await get_reaction(message,"123emoji")
             
    if author.id == IDs["Rachel"] or author.id == IDs["Trung"]:               #318366307169075201
        return await get_reaction(message,"123hearts")
    
    if author.id == IDs["Jessie"]:
        await get_reaction(message,"123jessie")
        await client.add_reaction(message,reactionsdict["lstgay"][0])
        await client.add_reaction(message,reactionsdict["lstgay"][1])
        await client.add_reaction(message,reactionsdict["lstgay"][2])
        return await get_reaction(message,"123jessie")
    
    for i in inmsg:
        if message.content == "?":
            return await get_reaction(message,"?")
        elif i in mess:
            return await get_reaction(message,i)
    


async def get_reaction(message,i):
    index = randint(0,len(reactionsdict[inmsg[i]]) - 1)
    try:
       await client.add_reaction(message,reactionsdict[inmsg[i]][index])
    except:
        if message.content.find('EMOJI_NAME'):
            for x in client.get_all_emojis():
                if x.id == reactionsdict[inmsg[i]][index]:
                    await client.add_reaction(message, x)
        
        
@client.command()
async def ping():
    await client.say('Pong!')


#@client.command(pass_context=True)
    
client.loop.create_task(change_status())
client.run(os.environ['BOT_TOKEN'])    
