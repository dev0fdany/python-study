import sys
from random import randint
def main():
    while True:
        try:
            user_input = input("Level: ")
            user_input = int(user_input)
            if user_input > 0:
                secret_number = randint(1,user_input)
                while True:
                    try:
                        user_guess = input("Guess: ")
                        user_guess = int(user_guess)
                        if user_guess > 0:
                            if user_guess > secret_number:
                                print("Too large!")
                            elif user_guess < secret_number:
                                print("Too small!")
                            else:
                                print("Just right!")
                                sys.exit(0)
                        else:
                            continue
                    except ValueError:
                        continue
        except ValueError:
            continue
if __name__ == "__main__":
    main()