def main():
    usr_Input = str(input("Input: "))
    twttr(usr_Input)

def twttr(usr_Input):
    output = ""
    for i in range (len(usr_Input)):
        if usr_Input[i].lower() in ["a","e","i","o","u"]:
            continue
        else:
            output += usr_Input[i]
    return(output)

if __name__ == "__main__":
    main()