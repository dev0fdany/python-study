
#main function
def main():
    usr_Input = int(input("Enter a number: "))
    if is_Even(usr_Input):
        print("It's even.")
    else:
        print("It's odd.")

def is_Even(x):
    return ( x % 2 == 0)
   
main()
