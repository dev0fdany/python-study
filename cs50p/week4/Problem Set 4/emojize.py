from emoji import emojize
def main ():
    userInput = input("INPUT: ")
    userInput = emojize(userInput)
    print(f"OUTPUT: {userInput}")
if __name__ == "__main__":
    main()
    

