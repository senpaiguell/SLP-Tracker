import discord
import requests
import asyncio
import random
from webserver import keep_alive
from replit import db

#get crypto data v
def getCryptoPrices(crypto):
  URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=smooth-love-potion&order=market_cap_desc&per_page=100&page=1&sparkline=false'
  r = requests.get(url=URL)
  data = r.json()




# putting the cryptocurrencies and their prices in db
  for i in range(len(data)):
    db[data[i]['id']] = data[i]['current_price']

  if crypto in db.keys():
    return db[crypto]
  else:
    return None

# check if a cryptocurrency is supported in this bot
def isCryptoSupported(crypto):
  if crypto in db.keys():
    return True
  else:
    return False
 
 

getCryptoPrices(0)
whack = 'binancecoin'
quack = 'smooth-love-potion'
client = discord.Client()


@client.event
async def on_ready():
#status
  print('you have logged in as Miguel')
#random status
async def ch_pr():
  await client.wait_until_ready()
  statuses = [f"SLP Price {getCryptoPrices(quack)} PHP",f"slp Price {getCryptoPrices(quack)} PHP",f"SLP Price {getCryptoPrices(quack)} PHP",f"SLp Price {getCryptoPrices(quack)} PHP"]

  while not client.is_closed():
    status = random.choice(statuses)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

    await asyncio.sleep(1)




#slp checker
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('slp'):
    if 'smooth-love-potion' in db.keys():
      await message.channel.send(f'The current price of SLP is: {getCryptoPrices(quack)} PHP')
  if message.content.startswith('!gl'):
    await message.channel.send("winstreak is coming, don't get tilted")
    await message.channel.send("https://media.giphy.com/media/WrNmpdgeJw5FCPKZto/giphy.gif")
  if message.content.startswith('goodluck'):
    await message.channel.send("Winstreak is coming bois!!!")
    await message.channel.send("https://media.giphy.com/media/TKvdUQROPwca2oxFWY/giphy.gif")
  

keep_alive()
client.loop.create_task(ch_pr())

client.run('OTA1ODEzMjMzMjAwNDA2NTU5.YYPiTw.E2BbwATtzoQvQzsHw6szeAr4gHk')