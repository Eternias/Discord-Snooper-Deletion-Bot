import discord
import os
import asyncio

bot = discord.Client()
@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))
@bot.event 
async def on_message(message):
	
	archive = bot.get_channel(975165873415401562)
	channel = message.guild.get_channel(975111004495183963)
	if (message.channel.name == 'ten-minute-chat'):
		await asyncio.sleep(10)
		await archive.send(message.author.name + " said: " + message.content)
		await message.delete()
	else:
		return

Token = os.environ['Bot_Token']

bot.run(Token)
#python keep_alive.py

