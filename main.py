import discord
import random
import os
import asyncio
from dotenv import load_dotenv


client = discord.Client()


@client.event
async def on_ready():
    """logs that the bot is online"""
    print('Successfully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content.lower())
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    #makes sure the bot cannot respond to itself
    if message.author == client.user: 
        return
    
    if message.channel.name == 'bot-command':
        if user_message.lower() == '.yo':
            await message.channel.send('sup nerd')
            return

    if user_message == '.anywhere':
        await message.channel.send('The first message')
        return

    if user_message== '.stutter':
        await message.channel.send(file=discord.File('stutter.jpg'))
        return

    if user_message== '.timewaste':
        await message.channel.send(file=discord.File(r"C:\Users\ebaba\OneDrive - Technological University Dublin\School_Work\DISCORD_BOT\dotBot\vids\timer.mp4"))
        return
    
    if user_message== '.coinflip':
        coin = random.randint(1,2)
        if coin == 1:
            await message.channel.send('heads')
            return
        else:
            await message.channel.send('tails')
            return

    #
    # Unfinished code below
    #
    # Description: recreates tictactoe to discord
    #
    # Current functionality: The bot can currently respond to one user input after entering the
    # initial command '.tictactoe'
    #
    # Future plan: implement a for loop that allows for multiple user inputs after the first
    #              make the update grid its own function
    #              fix aestetics 
    
    if user_message == '.tictactoe':
        background = ':blue_square:'':blue_square:'':blue_square:''\n'':blue_square:'':blue_square:'':blue_square:''\n'':blue_square:'':blue_square:'':blue_square:'
        x= ':regional_indicator_x:'
        o= ':regional_indicator_o:'
        await message.channel.send(background)
        await message.channel.send('Please enter what postion you want to go to from 1-9')   
        

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel and \
            msg.content in ['1','2','3','4','5','6','7','8','9']
        
        try:
            user_msg = await client.wait_for('message', check=check, timeout = 15.0)

        except asyncio.TimeoutError: 
            await message.channel.send('bot timedout: No reply sent')
            return                                         
        
        else:    
            grid = list(background)
            del grid[1:13]
            grid[0] = x
            background = ''.join(grid)
            await message.channel.send(background)

    
                


load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)