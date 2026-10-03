def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    size = len(s)
    # Length must be 2-6
    if size < 2 or size > 6:
        return False

    # First two characters must be letters
    if not s[:2].isalpha():
        return False

    # Only letters and numbers allowed
    if not s.isalnum():
        return False

    number_seen = False
    for char in s:
        if char.isdigit():
            if not number_seen:
                # First number cannot be 0
                if char == "0":
                    return False
                number_seen = True
        elif number_seen:
            # Letters after a number are not allowed
            return False
    return True
            
if __name__ == "__main__":
   main()