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
from lists import *
import permissions
from permissions import IDs
#

client = commands.Bot(command_prefix = '-!')
client.remove_command('help')
status = ['Rocky', 'x', 'Rachel']
randomstatus = 0
randomcounter = 0

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
    chance = randint(1,200)
    print(chance)
    mess = message.content.lower()
    global randomstatus
    global randomcounter
               
    if author.id == IDs["Rachel"] or author.id == IDs["Trung"]:               #318366307169075201
        return await get_reaction(message,"123hearts")
    
    
    if chance in range(1,2):
            if randomstatus == 0:
                randomstatus = 1
                await client.add_reaction(message,reactionsdict["lstrandomlol"][randomcounter])
                randomcounter += 1
                return
            
    if author.id == IDs["Vivian"]:
        chance = randint(100,200)
        if chance in range(199,200):
            if randomstatus == 0:
                randomstatus = 2
                for i in range(0,4):
                    await client.add_reaction(message,reactionsdict["lstnicevoice"][i])           
                randomcounter = 4
                return
            
    if author.id == IDs["Charlie"]:
        chance = randint(100,200)
        if chance in range(199,200):
            if randomstatus == 0:
                randomstatus = 3
                for i in range(0,4):
                    await client.add_reaction(message,reactionsdict["lstded"][i])           
                randomcounter = 4
                return
            
    if author.id == IDs["Rocky"]:
        chance = randint(1,10)
        if chance in range(1,2):
            for i in range(0, len(reactionsdict["lstrxr"]) - 1):
                await client.add_reaction(message,reactionsdict["lstrxr"][i])
            return
        
    if author.id == IDs["Nomi"]:
        chance = randint(1,1000)
        if chance in range(1,2):
            for i in range(0, len(reactionsdict["lstlips"]) - 1):
                await client.add_reaction(message,reactionsdict["lstrxr"][i])
            return
        
    if randomstatus == 1:
            try:
                await client.add_reaction(message,reactionsdict["lstrandomlol"][randomcounter])
                randomcounter += 1
                return
            except IndexError:
                randomstatus = 0
                randomcounter = 0
                return
                
    elif randomstatus == 2:
            try:
                await client.add_reaction(message,reactionsdict["lstnicevoice"][randomcounter])
                randomcounter += 1
                return
            except IndexError:
                randomstatus = 0
                randomcounter = 0
                return
                
    elif randomstatus == 3:
            try:
                await client.add_reaction(message,reactionsdict["lstded"][randomcounter])
                randomcounter += 1
                return
            except IndexError:
                randomstatus = 0
                randomcounter = 0
                return
                
    if author.id == IDs["Jessie"]:
        chance = randint(1,100)
        if chance == 9:           
            await client.add_reaction(message,reactionsdict["lstgay"][0])
            await client.add_reaction(message,reactionsdict["lstgay"][1])
            return await client.add_reaction(message,reactionsdict["lstgay"][2])
        elif chance in range(1,50):
            return await get_reaction(message,"123jessie")       
        
    if author.id == IDs["Owner"]:
        chance = randint(1,20)
        if chance == 11:
            return await get_reaction(message,reactionsdict["lstblue"][0])
    
    
    
    if message.content == "?":
        return await get_reaction(message,"123?")
    
    for i in inmsg:
        if i in mess:
            return await get_reaction(message,i)
        
    if chance in range(150,200): 
        return await get_reaction(message,"123emoji")
    
        
    


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
