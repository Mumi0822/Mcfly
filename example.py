import discord
from discord import guild
from discord.flags import Intents

client = discord.Client()
Grobal_ch_num = 0

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_guild_join(guild):
    await client.guild.text_channels[0].send('Thanks your inviting me!!!')
    return

@client.event
async def on_message(message):
    text_ch = message.guild
    if message.author == client.user:
        return
    if message.content.startswith('G/'):
        #Grobalchannelを指定
        i = 0
        while text_ch.text_channels:
            i+=1
            if message.content.startswitch('G/'+i):
                await print(i)
                Grobal_ch_num = i-1
                await print(Grobal_ch_num)
                return
        await message.channel.send('There is no channel!')
    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')

client.run('')
