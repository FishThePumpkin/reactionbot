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

#import listss
lstemoji = reactionsdict["lstemoji"]
lstuniemoji = []
lstjessie = reactionsdict["lstjessie"]
lsthearts = reactionsdict["lsthearts"]
lstoops = reactionsdict["lstoops"]
lstwink = reactionsdict["lstwink"]
lstthink = reactionsdict["lstthink"]
lstzzz = ['\U0001F634']
lsttsun = ['448817502089379852']
lstquestion = ['\U00002753']
lsttoxic = ['547680967397998642']
lstping = ['547683507690799114','547683506579439618','547683506625445888']
lstdash = ['551731555597549588']
lstgay = ['\U0001F1EC','\U0001F1E6','\U0001F1FE']
allwink = len(lstwink) - 1 
alltsun = len(lsttsun) - 1 
allquestion = len(lstquestion) - 1 
alltoxic = len(lsttoxic) - 1 
allping = len(lstping) - 1
alldash = len(lstdash) - 1 
allhearts = len(lsthearts) - 1 
allemoji = len(lstemoji) - 1 
alljessie = len(lstjessie) - 1

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
    ":GWchadThink:", "lstdash"
}

#lstemoji = lstjessie = lsthearts = lstoops = lstwink = lstthink = lstzzz = lsttsun = lstquestion = lsttoxic = lstping = lstdash = lstgay 
namelst = []
#lstlst = [lstemoji,lstjessie,lsthearts,lstoops,lstwink,lstthink,lstzzz,lsttsun,lstquestion,lsttoxic,lstping,lstdash,lstgay]
#namelst = ["lstemoji","lstjessie","lsthearts","lstoops","lstwink","lstthink","lstzzz","lsttsun","lstquestion","lsttoxic","lstping","lstdash","lstgay"]
#alllst = [allemoji,alljessie,allhearts,alloops,allwink,allthink,allzzz,alltsun,allquestion,alltoxic,allping,alldash,allgay]

for i in reactionsdict:
    namelst.append(i)

print(namelst)
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
    for i in reactions:
        if i in mess:
            index = randint(0,len(reactionsdict[inmsg[i]]))
            try:
                return await client.add_reaction(message,reactionsdict[inmsg[i]])
            except:
                if message.content.find('EMOJI_NAME'):
                 for x in client.get_all_emojis():
                    if x.id == reactionsdict[inmsg[i]][index]:
                        return await client.add_reaction(message, x)
        
    if 'wink' in message.content:
        wink = randint(0, allwink)
        return await client.add_reaction(message, lstwink[wink])
    elif 'baka' in message.content:
        tsun = randint(0, alltsun)
        if message.content.find('EMOJI_NAME'):
             for x in client.get_all_emojis():
                if x.id == lsttsun[tsun]:
                    return await client.add_reaction(message, x)
    elif message.content == '?':
        question = randint(0, allquestion)
        return await client.add_reaction(message, lstquestion[question])
    elif '<@547365819122712586>' in message.content: 
        ping = randint(0, allping)
        if message.content.find(':okay_hand:'):
             for x in client.get_all_emojis():
                if x.id == lstping[ping]:
                    return await client.add_reaction(message, x)
    elif ':GWsocksBlobAngeryPing:' in message.content:
        dash = randint(0, alldash)
        if message.content.find(':okay_hand:'):
             for x in client.get_all_emojis():
                if x.id == lstdash[dash]:
                    return await client.add_reaction(message, x)
    elif ':GWsocksThonkeryPing:' in message.content:
        dash = randint(0, alldash)
        if message.content.find(':okay_hand:'):
             for x in client.get_all_emojis():
                if x.id == lstdash[dash]:
                    return await client.add_reaction(message, x)
    elif ':GWcmeisterPeepoShrug:' in message.content:
        dash = randint(0, alldash)
        if message.content.find(':okay_hand:'):
             for x in client.get_all_emojis():
                if x.id == lstdash[dash]:
                    return await client.add_reaction(message, x)
    elif ':GWchadThink:' in message.content:
        dash = randint(0, alldash)
        if message.content.find(':okay_hand:'):
             for x in client.get_all_emojis():
                if x.id == lstdash[dash]:
                    return await client.add_reaction(message, x)
         
    elif author.id == "318366307169075201" or author.id == "328345368494342155":               #318366307169075201
        heart = randint(0, allhearts)
        return await client.add_reaction(message, lsthearts[heart])
    
    elif author.id == "290419231734890497":
        jessie = randint(0,alljessie)
        await client.add_reaction(message,lstjessie[jessie])
        await client.add_reaction(message,lstgay[0])
        await client.add_reaction(message,lstgay[1])
        await client.add_reaction(message,lstgay[2])
        jessie = randint(0,alljessie)
        return await client.add_reaction(message,lstjessie[jessie])
    
    if chance == 2: 
        emoji = randint(0, allemoji) 
        if message.content.find(':okay_hand:'):
             for x in client.get_all_emojis():
                if x.id == lstemoji[emoji]:
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
