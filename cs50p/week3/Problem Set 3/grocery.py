grocery_list = {}

def main():
    while True:
        try:
            item = input().upper()
            if item not in grocery_list:
                grocery_list[item] = 1
            elif item in grocery_list:
                grocery_list[item] = grocery_list[item] + 1
            else:
                continue
        except EOFError:
            break
    
    for theitem, how_much in grocery_list.items():
        print(f"{how_much}.{theitem}")



if __name__ == "__main__":
    main()
