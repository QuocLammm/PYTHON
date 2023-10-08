import random

def play_game():
    choices = ['Rock', 'Paper', 'Scissors']
    user_score = 0
    computer_score = 0
    rounds_to_win = 10 # tùy chỉnh round chơi bao nhiêu trận win
    

    for _ in range(rounds_to_win):
        print(f"\nCurrent Score - You: {user_score}, Computer: {computer_score}")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        user_choice = int(input("Enter your choice (1-3): "))
        if user_choice not in [1, 2, 3]:
            print("Invalid choice. Please choose again.")
            continue

        user_choice = choices[user_choice - 1]
        computer_choice = random.choice(choices)

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    if user_score > computer_score:
        print("You won the game!")
    elif user_score < computer_score:
        print("Computer won the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
