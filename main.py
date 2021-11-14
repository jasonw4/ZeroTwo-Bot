import discord
import os
import requests
import json
import random
from datetime import datetime
import pytz


client = discord.Client()



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - ZeroTwo, obviously..."
  return quote

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  username = str(message.author).split('#')[0]

  tz_NY = pytz.timezone('America/New_York') 
  datetime_NY = datetime.now(tz_NY)
 
  list_of_commands = ['-hello', '-help', '-time', '-date', 'inspireme02']
  images = ['zerotwo.jpeg', '902675.png', '904880.png', '908470.jpg', '901811.png']
  gifs = ['zerotwo1.gif', 'original.gif']
  message_text = message.content.upper()
  if message.author == client:
    return

  elif message.content.startswith('-hello'):
    await message.channel.send('Heyyy~')

  elif message.content.startswith('-inspireme02'):
    quote = get_quote()
    await message.channel.send(quote)
  elif message.content.startswith('-image'):
    await message.channel.send(file=discord.File(random.choice(images)))
  elif message.content.startswith('-gif'):
    await message.channel.send(file=discord.File(random.choice(gifs)))
  elif message.content.startswith('-time'):
    await message.channel.send(datetime_NY.strftime("%H:%M:%S"))
    if 0 <= int(datetime_NY.hour) <= 4:
      await message.channel.send('Go to sleep...zzzz')
  elif message.content.startswith('-date'):
    await message.channel.send(datetime_NY.strftime("%m/%d/%Y"))
  elif message.content.startswith('-help'):
    await message.channel.send('Here are a list of commands, created by Zero Two:')
    await message.channel.send(list_of_commands)
      
  sadkeys = ['SAD', 'DEPRESSED','UNHAPPY', 'MISERABLE', 'HEARTBROKEN']
  sadquotes = [f'It ok {username}~', f'You got this {username}!', 'Darling, wanna run away with me?']
  for x in sadkeys:
    if x in message_text:
      await message.channel.send(random.choice(sadquotes))
  

  happykeys = ['HAPPY', 'CHEERFUL', 'CONTENT', 'DELIGHTED', 'THRILLED']
  happyquotes = [f'Good for you {username}!', 'I feel the same.', "It's an amazing feeling, isn't it ~"]
  for x in happykeys:
    if x in message_text:
      await message.channel.send(random.choice(happyquotes))


      
  zt = [' HEY ZEROTWO', ' HEY ZERO TWO']
  for x in zt:
    if x in message_text:
      await message.channel.send("How's it going, darling? ~~")
  

  cry = ['CRY', 'CRIED', 'CRYING']
  for x in cry:
    if x in message_text:
      await message.channel.send("It's been a long time since I last saw a human cry.")

  tired = ['LAZY', 'TIRED', 'SLEEPY']
  for x in tired:
    if x in message_text:
        await message.channel.send('Go rest, darling ~~')


  ztz = ["HOW'S IT GOING", "HOW'S IT GOING ZERO TWO", "WHAT'S UP ZERO TWO", "HOWS IT GOING", "HOWS IT GOING ZERO TWO","WHATS UP ZERO TWO", "WHAT'S UP", "WHATS UP", "HOW ARE YOU" ]
  for x in ztz:
    if x in message_text:
      await message.channel.send(f"Everything is lovely here, {username} ~~")



  

  if message.content.startswith('-zerotoint'):
    numphrases = ["That's the number of pizza slices I ate today ~burp~", "What an interesting number...", "That's more than the amount of pure demons left in the world..."]
    await message.channel.send(random.randint(0, 999))
    await message.channel.send(random.choice(numphrases))
  
  for i in range(10000000):
    if message.author == client:
      return
    elif message_text == str(i):
      if i%2 == 0:
        await message.channel.send("This number is even, darling.")
      else:
        await message.channel.send("This number is odd. Oddly satisfying ~")







          


  

    
          
    
        
      
    


    





  


      






client.run(os.getenv('TOKEN'))

