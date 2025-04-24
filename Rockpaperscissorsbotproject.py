if message.content.startswith('$RPS'):
            rock = 1
            paper = 2
            scissors = 3

            discord.Message ('Rock, paper scissors, shoot!')
            discord.Message ('1. Rock✊')
            discord.Message ('2. paper🫳')
            discord.Message ('3. scissors✌️?')

            user_choice = int((input)('Choose 1 for rock, 2 for paper, 3 for scissors:'))
            if user_choice == 1:
              discord.Message ('you chose rock')  
            elif user_choice == 2:
              discord.Message ('you chose Paper')
            else:
              discord.Message ('you chose scissors')

            Code_choice = random.randint (1 , 3)
            if Code_choice == 1:
              discord.Message ('Bot chose rock')
            elif Code_choice == 2:
              discord.Message ('Bot chose paper')
            else:
              discord.Message ('Bot chose scissors')

            while Code_choice == (1) and user_choice == (1):
              discord.Message ('draw, again!')
              discord.Message ('Rock, paper scissors, shoot!')
              discord.Message ('1. Rock✊')
              discord.Message ('2. paper🫳')
              discord.Message ('3. scissors✌️?')
user_choice = int((input)('Choose 1 for rock, 2 for paper, 3 for scissors'))

if user_choice == 1:
              discord.Message ('you chose rock')
elif user_choice == 2:
              discord.Message ('you chose Paper')
else:
              discord.Message ('you chose scissors')
Code_choice = random.randint (1 , 3)
if Code_choice == 1:
              discord.Message ('Bot chose rock')
elif Code_choice == 2:
              discord.Message ('Bot chose paper')
else:
              discord.Message ('Bot chose scissors')

while Code_choice == (2) and user_choice == (2):
              discord.Message ('draw, again!')
              discord.Message ('Rock, paper scissors, shoot!')
              discord.Message ('1. Rock✊')
              discord.Message ('2. paper🫳')
              discord.Message ('3. scissors✌️?')
user_choice = int((input)('Choose 1 for rock, 2 for paper, 3 for scissors'))
if user_choice == 1:
               discord.Message ('you chose rock')
elif user_choice == 2:
              discord.Message ('you chose Paper')
else:
              discord.Message ('you chose scissors')
Code_choice = random.randint (1 , 3)
if Code_choice == 1:
              discord.Message ('Bot chose rock')
elif Code_choice == 2:
              discord.Message ('Bot chose paper')
else:
              discord.Message ('Bot chose scissors')

while Code_choice == (3) and user_choice == (3):
              discord.Message ('draw, again!')
              discord.Message ('Rock, paper scissors, shoot!')
              discord.Message ('1. Rock✊')
              discord.Message ('2. paper🫳')
              discord.Message ('3. scissors✌️?')
user_choice = int((input)('Choose 1 for rock, 2 for paper, 3 for scissors'))
if user_choice == 1:
              discord.Message ('you chose rock')
elif user_choice == 2:
              discord.Message ('you chose Paper')
else:
               discord.Message ('you chose scissors')
Code_choice = random.randint (1 , 3)
if Code_choice == 1:
              discord.Message ('Bot chose rock')
elif Code_choice == 2:
              discord.Message ('Bot chose paper')
else:
              discord.Message ('Bot chose scissors')

#rock = 1 
#paper = 2 
#scissors = 3 
if Code_choice == 1 and user_choice == 3:
              discord.Message ('you lose')
elif Code_choice == 2 and user_choice == 1:
              discord.Message ('you lose')
elif Code_choice == 3 and user_choice == 2:
              discord.Message ('you lose')
elif user_choice == 1 and Code_choice == 3:
              discord.Message ('Rock Beats scissors, YOU WIN!')
elif user_choice == 2 and Code_choice == 1:
              discord.Message ('paper covers rock, YOU WIN!')
elif user_choice == 3 and Code_choice == 2:
              discord.Message ('scissors cut paper, YOU WIN!')