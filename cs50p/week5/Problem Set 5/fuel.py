def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break


def convert(fraction):
    numerator, denominator = fraction.split("/")

    numerator = int(numerator)
    denominator = int(denominator)

    if denominator == 0:
        raise ZeroDivisionError 
    elif numerator < 0 or numerator > denominator:
        raise ValueError
   
    percentage = round((numerator / denominator) * 100)

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()