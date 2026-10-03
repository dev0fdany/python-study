
def main():
    usr_Input = str(input("camelCase: "))
    snake_case = ""
    for i in range (len(usr_Input)):
            if usr_Input[i].isupper():
                snake_case += "_"
                snake_case  += usr_Input[i].lower()
            else:
                snake_case += usr_Input[i]
                
    print(f"snake_case: {snake_case}")

main()

    