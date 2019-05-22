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

reactions = ["wink","baka","toxic","<@547365819122712586>",":GWsocksBlobAngeryPing:",":GWsocksThonkeryPing:",":GWcmeisterPeepoShrug:",":GWchadThink:"]

inmsg = {
    "wink": "lstwink",
    "baka": "lsttsun",
    #"?": "lstquestion",
    "toxic": "lsttoxic",
    "<@547365819122712586>": "lstping",
    ":GWsocksBlobAngeryPing:": "lstdash",
    ":GWsocksThonkeryPing:": "lstdash",
    ":GWcmeisterPeepoShrug:": "lstdash",
    ":GWchadThink:": "lstdash"
}

#lstemoji = lstjessie = lsthearts = lstoops = lstwink = lstthink = lstzzz = lsttsun = lstquestion = lsttoxic = lstping = lstdash = lstgay 
#namelst = []
#lstlst = [lstemoji,lstjessie,lsthearts,lstoops,lstwink,lstthink,lstzzz,lsttsun,lstquestion,lsttoxic,lstping,lstdash,lstgay]
#namelst = ["lstemoji","lstjessie","lsthearts","lstoops","lstwink","lstthink","lstzzz","lsttsun","lstquestion","lsttoxic","lstping","lstdash","lstgay"]
#alllst = [allemoji,alljessie,allhearts,alloops,allwink,allthink,allzzz,alltsun,allquestion,alltoxic,allping,alldash,allgay]

#for i in reactionsdict:
    #namelst.append(i)

#print(namelst)
 #   lstlst[i] = reactionsdict[namelst[i]]
  #  alllst[i] = len(lstlst[i]) - 1

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
            get_reaction(message,i)
            
    if message.content == '?':
        index = randint(0, len(reactionsdict["lstquestion"]) - 1)
        return await client.add_reaction(message, reactionsdict["lstquestion"][index])
         
    elif author.id == "318366307169075201" or author.id == "328345368494342155":               #318366307169075201
        index = randint(0, len(reactionsdict["lsthearts"]) - 1)
        return await client.add_reaction(message, reactionsdict["lsthearts"][index])
    
    elif author.id == "290419231734890497":
        index = randint(0, len(reactionsdict["lstjessie"]) - 1)
        await client.add_reaction(message,reactionsdict["lstjessie"][index])
        await client.add_reaction(message,reactionsdict["lstgay"][0])
        await client.add_reaction(message,reactionsdict["lstgay"][1])
        await client.add_reaction(message,reactionsdict["lstgay"][2])
        index = randint(0, len(reactionsdict["lstjessie"]) - 1)
        return await client.add_reaction(message,reactionsdict["lstjessie"][index])
    
    if chance == 2: 
        index = randint(0, len(reactionsdict["lstemoji"]) - 1) 
        if message.content.find(':okay_hand:'):
             for x in client.get_all_emojis():
                if x.id == reactionsdict["lstemoji"][index]:
                    return await client.add_reaction(message, x)  

async def get_reaction(message,i):
    index = randint(0,len(reactionsdict[inmsg[i]]) - 1)
    try:
       return await client.add_reaction(message,reactionsdict[inmsg[i]]
    except:
        if message.content.find('EMOJI_NAME'):
        for x in client.get_all_emojis():
            if x.id == reactionsdict[inmsg[i]][index]
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
