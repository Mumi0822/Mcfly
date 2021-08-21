import discord
from discord import guild
from discord.flags import Intents

client = discord.Client()

Grobal_ch_name =""

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_guild_join(guild):
    await guild.text_channels[1].send('Thanks your inviting me!!!')
    return

@client.event
async def on_message(message):
    text_ch = Intents.guild.text_channels
    if message.author == client.user:
        return
    if message.content.startswith('G/'):
        i = 0
        while(text_ch[i]):
            i+=1
            if message.content.startswitch('G/'+i):
                print(i)
                Grobal_ch_name = i
                print(Grobal_ch_name)
    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')



client.run('')
