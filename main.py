
import random


# NUMBER GUESSING GAME
def number_guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")

    number = random.randint(1, 100)
    attempts = 0

    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")

            elif guess > number:
                print("Too high! Try again.")

            else:
                print("Congratulations! You guessed correctly.")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")


# FILE-BASED WORD COUNTER
def word_counter():
    print("\n--- WORD COUNTER ---")

    filename = input("Enter text file name (example: sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = text.split()
        characters = len(text)
        lines = len(text.splitlines())

        print("\n--- WORD COUNT RESULT ---")
        print("Total words:", len(words))
        print("Total characters:", characters)
        print("Total lines:", lines)

    except FileNotFoundError:
        print("File not found!")
        print("Please create the text file in the project folder.")

    except OSError:
        print("Unable to read the file.")


# MAIN MENU
def main():
    while True:
        print("\n================================")
        print(" NUMBER GUESSING GAME")
        print("       & WORD COUNTER")
        print("================================")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
