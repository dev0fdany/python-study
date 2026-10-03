from datetime import date
import sys
import inflect



def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid Date.")

    p = inflect.engine()
    today_date = date.today()
    age_in_days = today_date - birth_date
    age_in_minute = age_in_days.days * 24 * 60
    words = p.number_to_words(age_in_minute)
    words = words.replace("and", "").capitalize()
    print(f"{words}")




if __name__ == "__main__":
    main()
