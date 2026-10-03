months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").title()
        try:
            if "/" in date: #MM/DD/YYYY
                month_number, day , year = date.split("/")
                month_number = int(month_number)
                day = int(day)
                year = int(year)
                    
                if 1<= month_number <= 12  and 1<= day <= 31:
                    break
        except ValueError:
                continue
        if "," in date: #MM DD, YYYY
            try:
                if " " in date:
                    month, day_with_comma , year = date.split(" ")
                    day = int(day_with_comma.strip(","))
                    month_number = int(months.index(month) + 1)
                    year = int(year)
                    if 1<= day <= 31:
                        break
            except ValueError:
                continue
        else:
            continue
    print(f"{year}-{month_number:02}-{day:02}") #YYYY-MM-DD

if __name__ == "__main__":
    main()