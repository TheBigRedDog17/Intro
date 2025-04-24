import random
#helper turns 1/2/3 into strings
CHOICE_NAMES = {
  1: "rock",
  2: "paper",
  3: "scissors"
}

  
#This will determine whether a draw has occured, and if no draw is found will determine the winner
def determine_winner (user, bot):
  if user == bot:
        return None
  #rock (1) beats scissors(3), paper(2) beats rock(1) and scissors(3) beats paper(2)
  wins = {
    (1, 3)
    (2, 1)
    (3, 2)
  }
  return "user" if (user, bot) in wins else "bot"

def rock_paper_scissors():
  while True:
  #Player picks a input and this is used by the player 
    try:
        user_choice = int((input)("Choose 1 for rock, 2 for paper and 3 for scissors: "))
        if user_choice not in CHOICE_NAMES: raise ValueError
    except ValueError:
        print("Invalid choice. Please enter 1, 2 or 3. \n")
        continue
    print(f"You chose {CHOICE_NAMES[user_choice]}")
    
    bot_choice = random.randint (1,3)
    print(f"Bot chose {CHOICE_NAMES[bot_choice]}")

    result = determine_winner(user_choice, bot_choice)
    if result is None:
        print("It's a draw! Let's go again.\n")
        continue
    elif result == "user":
       print("🎉 You win!")
    else:
       print("😢 Bot wins!")
    break
if __name__ == "__main__":
   rock_paper_scissors()
