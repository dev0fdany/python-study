import sys
from random import choice
from pyfiglet import Figlet
#random.choice(fontslist) for random selection of font
def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        rnd_font = choice(fonts)
        user_input = input("INPUT: ")
        figlet.setFont(font=rnd_font)
        print("OUTPUT:\n\n"+ figlet.renderText(user_input))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in fonts:
                user_font = sys.argv[2]
                figlet.setFont(f=user_font)
                user_input = input("INPUT: ")
                print("OUTPUT:\n\n"+ figlet.renderText(user_input))
            else:
                print("Invalid Input.")
                sys.exit()
        else:
            print("Invalid Input.")
            sys.exit()
    else:
        print("Invalid Input.")
        sys.exit()



if __name__ == "__main__":
    main()