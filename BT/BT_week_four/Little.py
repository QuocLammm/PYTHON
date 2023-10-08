import random

def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        x, y = generate_integer(level)
        question = f"{x} + {y} = "
        correct_answer = x + y

        attempts = 0
        while attempts < 3:
            user_answer = input(question)
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                    correct_answers += 1
                    break
                else:
                    print("EEE. Try again.")
                    attempts += 1
            except ValueError:
                print("EEE. Try again.")
                attempts += 1

        if attempts == 3:
            print(f"The correct answer is: {correct_answer}")

    print(f"You got {correct_answers} out of 10 correct.")

def get_level():
    while True:
        try:
            level = int(input("Choose a level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    if level == 1:
        digits = 1
    elif level == 2:
        digits = 2
    else:
        digits = 3

    x = random.randint(10 ** (digits - 1), 10 ** digits - 1)
    y = random.randint(10 ** (digits - 1), 10 ** digits - 1)
    return x, y

if __name__ == "__main__":
    main()
