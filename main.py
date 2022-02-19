import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands


client = discord.Client()


@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'bot-command':
        if user_message.lower() == '.yo':
            await message.channel.send('sup nerd')
            return

    if user_message.lower() == '.anywhere':
        await message.channel.send('The first message')
        return

    if user_message.lower()== '.stutter':
        await message.channel.send(file=discord.File('stutter.jpg'))
        return

    if user_message.lower()== '.timewaste':
        await message.channel.send(file=discord.File(r"C:\Users\ebaba\OneDrive - Technological University Dublin\School_Work\DISCORD_BOT\dotBot\vids\timer.mp4"))
        return

load_dotenv()
TOKEN = os.getenv("TOKEN")
client.run(TOKEN)