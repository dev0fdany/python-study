import random

def main():
    WORDS = """
    ant baboon badger bat bear beaver camel cat clam cobra cougar 
    coyote crow deer dog donkey duck eagle ferret fox frog goat 
    goose hawk lion lizard llama mole monkey moose mouse mule newt 
    otter owl panda parrot pigeon python rabbit ram rat raven 
    rhino salmon seal shark sheep skunk sloth snake spider 
    stork swan tiger toad trout turkey turtle weasel whale wolf 
    wombat zebra
    """.split()    
    word = random.choice(WORDS)
    guess = []
    guess_correct = []
    word_seperate = []
    for letter in word:
        word_seperate.append(letter) 
    uniq_letter = set(word_seperate)


    while True: 
            correct = 0 
            guess_count = 0
            try:
                usr_char = input("Enter letter to guess: ").lower()
                if not usr_char.isalpha():
                   exit() 
                guess.append(usr_char) 
                if usr_char in uniq_letter:
                    guess_correct.append(usr_char)
                for letter in uniq_letter:
                    if letter in set(guess_correct):
                        correct += 1
                if correct == len(uniq_letter):
                        print("YOU WON!")
                        exit()
                elif word in guess:
                        print("YOU WON!")
                        exit()
                else:
                    for letter in word_seperate:
                        if letter in guess:
                            print(letter,end="",sep=",")
                        else:
                            print(f"_",end="")
                unique_guess = list(dict.fromkeys(guess))
                for letter in unique_guess:
                    if guess_count >= 6:
                        print(hangman(guess_count))
                        print("YOU LOST!")
                        print(word)
                        exit()
                    else:
                        if not letter in word_seperate:
                            if letter == unique_guess[-1]:
                                print(hangman(guess_count))
                            guess_count += 1

                print()
        
                
            except ValueError:
                exit()

def hangman(count):

    hangman_states = [r"""
  ┌───┐
  │   │
      │
      │
      │
      │
══════╧══""",r"""
  ┌───┐
  │   │
  O   │
      │
      │
      │
══════╧══""",r"""

  ┌───┐
  │   │
  O   │
 /    │
      │
      │
══════╧══""",r"""
  ┌───┐
  │   │
  O   │
 /║   │
      │
      │
══════╧══""",r"""
  ┌───┐
  │   │
  O   │
 /║\  │
      │
      │
══════╧══""",r"""
  ┌───┐
  │   │
  O   │
 /║\  │
 /    │
      │
══════╧══""",r"""
  ┌───┐
  │   │
  O   │
 /║\  │
 / \  │
      │
══════╧══"""]
    return hangman_states[count]

if __name__ == "__main__":
    main()
