
def main():
    usr_Input = str(input("Greeting: ")).title()

def greeting(usr_Input):
    if usr_Input.startswith("Hello"):
        return(f"$0")
    elif usr_Input.startswith("H"):
        return(f"$20")
    else:
        return(f"$100")

if __name__ == "__main__":
    main()