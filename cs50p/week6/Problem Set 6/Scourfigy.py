import sys
import csv

def main():
    try:
        if len(sys.argv) == 1:
            print("Too few command-line arguments.")
            sys.exit()
        elif len(sys.argv) > 3:
            print("Too many command-line arguments.")
            sys.exit()
        else:
            if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
                print("Not a csv file.")
            else:
                # This stores the full name and the house.
                csv_variable = []
                csv_new_file = []
                names_list = []
                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        # This appends a dictionary to a file.
                        csv_variable.append({"full_name":row["name"], "house":row["house"]})
                    for row in csv_variable:
                        last_name, first_name = row["full_name"].split(",")
                        last_name = last_name.strip(" ")
                        first_name = first_name.strip(" ")
                        csv_new_file.append({"first_name": first_name, "last_name": last_name, "house":row["house"]})
                    with open(sys.argv[2], "w") as newcsv:
                            # specifing the fieldnames for columns
                            writer = csv.DictWriter(newcsv, fieldnames=["first_name","last_name","house"])
                            # writing the header for colums
                            writer.writeheader()
                            # This write the whole list of dictionaries to the new file.
                            writer.writerows(csv_new_file) 
    except FileNotFoundError:
        print("File does not exist.")
        sys.exit()


if __name__ == "__main__":
    main()