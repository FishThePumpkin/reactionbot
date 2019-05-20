import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
from random import *
import os
from discord.utils import get

client = commands.Bot(command_prefix = '-!')
client.remove_command('help')
status = ['Rocky', 'x', 'Rachel']
lstemoji = ['546236381085696014','355674756592304129','526994450044420097','526980435646087178','527015911261995037','481655460370448385','403046003932004352','387445113422479360','448817502089379852','399738095886532619','445199594780098560','490546759274201108','545457687912120321','545458529247690762','547565823842189333','547567174672187393','547567191571038208','547567211699765297','547567233673723926','547567254116761601','547567026076385285','547567041687846933','547567062424223771','547567082930307090','547567103499173899','547567120951672872','547567139637166090','547567158243360779']
lstuniemoji = []
lstjessie = ['🐣','🐥','🐛','🐍','🐙','🌸','🌟','✨','⭐️','💫','🌈','☁️','🍉','🍋','🍈','🍓','🍑','🍒','🍔','🍟','🍕','🥪','🍣','🥟','🍡','🎂','🍰','🍫','🍬','🍭','🍮','🍦','🍵','🎀','💎']
lsthearts = ['❤','\U00002661','\U00002763','\U0001F493','\U0001F494','\U0001F496','\U0001F497','\U0001F498','\U0001F49A','\U0001F49B','\U0001F49C','\U0001F49D','\U0001F49F','\U0001F5A4','\U0001F9E1']
lstoops = ['\U0001F605']
lstwink = ['\U0001F609','\U0001F61C','\U0001F61B','\U0001F635']
lstthink = ['\U0001F928','\U0001F914','\U0001F636','\U0001F60F','\U0001F62C']
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
    elif 'toxic' in message.content:
        toxic = randint(0, alltoxic)
        if message.content.find('EMOJI_NAME'):
             for x in client.get_all_emojis():
                if x.id == lsttoxic[toxic]:
                    return await client.add_reaction(message, x)
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
