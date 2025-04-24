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
        
        
        if message.content.startswith('$RPS'): #command for Rock paper scissor
          await message.channel.send('Rock Paper, Scissors, Shoot!') , Player_choice = int(input('Choose $1 for rock, $2 for paper, or $3 for scissors'))
        
        Rock = 1
        Paper = 2 
        Scissors = 3
        Bot_Choice = random.randint (1 , 3)
        
        if message.content.startswith('$1'):
          await message.channel.send('You chose Rock')
        elif message.content.startswith('$2'):
          await message.channel.send('You chose Paper')
        else:
          await message.channel.send('You chose Scissors')
          Bot_Choice = random.randint (1 , 3)
        if message.content.startswith ('$'):
          await message.channel.send(Bot_Choice)
        if (Bot_Choice) == Player_choice:
           await message.channel.send('It`s a draw, Again?')
        elif (Bot_Choice) == 1 and Player_choice == 3:
         await message.channel.send('YOU LOSE')
        elif (Bot_Choice) == 2 and Player_choice == 1:
           await message.channel.send('YOU LOSE')
        elif (Bot_Choice) ==3 and Player_choice == 2:
           await message.channel.send('YOU LOSE')

                   


        
        
    
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run ('') 