
#main function
def main():
    usr_Input = input()
    convert(usr_Input)

def convert(input_covt):
    input_covt = input_covt.replace(":(","☹️").replace(":)","🙂")
    print(input_covt)

main()
