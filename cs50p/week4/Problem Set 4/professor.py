import random


def main():
    level = get_level()
    tries = 0
    while True:
        answer, question = generate_integer(level)
        answer = str(answer)
        try:
            user_guess = input(question)
            if user_guess == answer:
                continue
            else:
                while(user_guess != answer):
                    tries += 1
                    print("EEE\n")
                    user_guess = input(question)
                    if user_guess == answer:
                        tries = 0
                        break
                    elif user_guess!= answer and tries == 2:
                        print("EEE\n")
                        print(f"{question} {answer}")
                        tries = 0
                        break
                    continue
        except EOFError:
            break 





def get_level():
    while True:
            try:
                level = input("Level: ")
                level = int(level)
                if level > 0 and level <= 3:
                    return level
                else:
                    continue
            except ValueError:
                break


def generate_integer(level):
    if level == 1:
        start, stop = 1, 10
    elif level == 2:
        start, stop = 1, 20
    else:
        start, stop = 1, 30
    
    numbr1 = random.randint(start,stop)
    numbr2 = random.randint(start,stop)
    
    answer = numbr1+numbr2
    question = f"{numbr1} + {numbr2} = "
    return answer,question

if __name__ == "__main__":
    main()
