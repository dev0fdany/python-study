

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            numerator , denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            if check_fraction(numerator,denominator):
                fuel_percentage(numerator,denominator)
            else:
                continue
        except ValueError:
            continue
        else:
            break


def check_fraction(numerator,denominator):
    if numerator >= 0:
        if numerator >denominator:
            return False
        else:
            return True
        return True
    else:
        return False

def fuel_percentage(numerator,denominator):
    try:
        percentage = round((numerator/denominator)*100)
        
        if(percentage<1):
            print("E")
        elif(percentage>99):
            print("F")
        else:
            print(percentage,"%",sep='')
    except ZeroDivisionError:
        return False
    else:
        return True


if __name__ == "__main__":
    main()