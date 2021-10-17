import discord

TOKEN = '' #Add your discord Token here
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(message)

client.run(TOKEN)