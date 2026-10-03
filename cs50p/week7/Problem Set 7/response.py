import sys
import validators

def main():
    print(check(input("What's your email address? ")))



def check(s):
    if validators.email(s):
        return f"Valid."
    else:
        return f"Invalid."

if __name__=="__main__":
    main()