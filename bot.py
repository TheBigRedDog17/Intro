import discord
import requests
import json
import random

def get_meme():
  response = requests.get ('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme me'):
            await message.channel.send(get_meme())

        if message.content.startswith('$hello'):
            await message.channel.send('What up, Homie')

        if message.content.startswith('$Glaze me'):
          glaze = random.randint (1, 3)
        if glaze == 1:
          await message.channel.send('Wow, Your killing it, bro!') 
        if glaze == 2:
          await message.channel.send('You were born to do more than just play games bro!')
        if glaze == 3:
          await message.channel.send('Either you run the day, or the day runs you.')

        
        
    
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run ('') 