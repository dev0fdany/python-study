
#main function
def main():
    usr_Input = str(input("Greeting: ")).title()
    
    if usr_Input.startswith("Hello"):
        print("$0")
    elif usr_Input.startswith("H"):
        print("$20")
    else:
        print("$100")
main()