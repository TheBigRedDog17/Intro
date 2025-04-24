import random

# map numbers to names
CHOICE_NAMES = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

def determine_winner(user_choice, bot_choice):
    """Return 'user' if the user wins, 'bot' if the bot wins, or None on draw."""
    # draw
    if user_choice == bot_choice:
        return None

    # winning combinations: (winner, loser)
    wins = {
        (1, 3),  # Rock beats Scissors
        (2, 1),  # Paper beats Rock
        (3, 2),  # Scissors beats Paper
    }

    return "user" if (user_choice, bot_choice) in wins else "bot"

def rock_paper_scissors():
    """Play one round of Rock-Paper-Scissors (replay on draw)."""
    while True:
        # get & validate user input
        try:
            user_choice = int(input("Choose 1 for Rock, 2 for Paper, 3 for Scissors: "))
            if user_choice not in CHOICE_NAMES:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.\n")
            continue

        print(f"\nYou chose {CHOICE_NAMES[user_choice]}")

        # bot picks
        bot_choice = random.randint(1, 3)
        print(f"Bot chose {CHOICE_NAMES[bot_choice]}")

        # decide
        result = determine_winner(user_choice, bot_choice)
        if result is None:
            print("It's a draw! Let's play again.\n")
            continue
        elif result == "user":
            print("🎉 You win!")
        else:
            print("😢 Bot wins!")
        break

if __name__ == "__main__":
    print("Welcome to Rock-Paper-Scissors!\n")
    rock_paper_scissors()
    print("Thanks for playing!")