import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
from random import *
import os
from discord.utils import get

client = commands.Bot(command_prefix = "-")
client.remove_command('help')
status = ['o', 'w', 'o']
lstemoji = ['546236381085696014','526994450044420097','526980435646087178','527015911261995037','481655460370448385','403046003932004352','387445113422479360','448817502089379852','399738095886532619','445199594780098560','490546759274201108','545457687912120321','545458529247690762']
lstuniemoji = []

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(2)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Online!'))
    print("Bot is ready")

@client.event
async def on_message(message):
    #rachel
    author = message.author
    if author.id == "318366307169075201":
        return await client.add_reaction(message, '❤')
    #chance
    chance = randint(1,15)
    if chance == 2:
        allemoji = len(lstemoji) - 1 
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
