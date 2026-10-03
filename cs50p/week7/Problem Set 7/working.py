import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches:= re.search(r"(1[0-2]|[1-9])(?::([0-5]\d))?\s+AM\s+to\s+(1[0-2]|[1-9])(?::([0-5]\d))?\s+PM", s):
        hour_am = matches.group(1)
        minute_am = matches.group(2)
        hour_pm = matches.group(3)
        minute_pm = matches.group(4)
    
        if minute_am is None:
            minute_am = "00"
        if minute_pm is None:
            minute_pm = "00"

        try:
            hour_am = int(hour_am)
            hour_pm = int(hour_pm)
        except ValueError:
            print('invalid input!')
            sys.exit()

        if hour_am == 12:
            hour_am = 0 # remember to display this as 00
        if hour_pm >= 1 and hour_pm <= 11:
            hour_pm +=12

        return(f"{hour_am:02d}:{minute_am} to {hour_pm:02d}:{minute_pm}")
    else:
        print("invalid input!")
        sys.exit()


if __name__ == "__main__":
    main()