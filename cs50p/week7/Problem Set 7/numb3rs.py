import re
import sys


def main():
    ipv4 = input("IPv4 Address: ").strip()
    # Validating
    is_valid = validate(ipv4)
    print(is_valid)

def validate(ipv4):
    # Writing the regex is actually difficult 
    # 2[0-4]\d means 2 and any number from 0-4 and then any number from 0-9 basically setting a range from 200-249
    # 1\d{2} means 1 and any two digits number
    # [1-9]\d means any one digit or 2 digit number
    if re.search(r"^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$", ipv4 ):
        return True
    else:
        return False



if __name__ == "__main__":
    main()