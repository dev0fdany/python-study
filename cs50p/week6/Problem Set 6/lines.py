import sys

def main():
    while True:
        try:
            if len(sys.argv) == 1:
                print("Too few command-line arguments.")
            elif len(sys.argv) > 2:
                print("Too many command-line arguments.") 
            else:
                if not sys.argv[1].endswith(".py"):
                    print("Not a python file.")
                    sys.exit()
                else:
                   copy_file = []
                   count_lines = 0
                   with open(sys.argv[1]) as thepythonfile:
                       for line in thepythonfile:
                            if not line.isspace():
                                copy_file.append(line)
                            else:
                                continue

                       for line in copy_file:
                           if line.startswith("#"):
                                continue
                           else:
                               count_lines += 1
                       print(count_lines) 
                       sys.exit()

        except FileNotFoundError:
            print("File does not exist.")
            sys.exit()

if __name__ == "__main__":
    main()