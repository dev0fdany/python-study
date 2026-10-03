import sys
import inflect
def main():
    names_list = []
    p = inflect.engine()
    while True:
        try:
            theNameEntered = input("Name: ").title()
            if theNameEntered not in names_list:
                names_list.append(theNameEntered)
            elif theNameEntered in names_list:
                continue
        except EOFError:
            break

    print("Adieu, adieu to "+p.join(names_list)) 


if __name__ == "__main__":
    main()