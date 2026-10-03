import sys
from tabulate import tabulate
import csv
def main():
    try:
        if len(sys.argv) < 1:
            print("Too few command-line arguments.")
            sys.exit()
        elif len(sys.argv) > 2:
            print("Too many command-line arguments.")
        else:
            # This is a list
            menu = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                # csv module took care of spliting and removing trailing white spaces
                for item ,price_small ,price_large in reader:
                    # This is a dictionary
                    menu_item = {"item": item , "price_small": price_small, "price_large": price_large}
                    # Appending a dict to a list
                    menu.append(menu_item)
            # Just looked at the documentation and just put the list of dictionaries, it worked!!
            print(tabulate(menu, tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist.")
        sys.exit()



if __name__ == "__main__":
    main()