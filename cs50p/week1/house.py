
name = str(input("What's your name? ")).title()

match name:
    case "Harry" | "Ron" | "Herminoe":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
       print("uhh.. Who?")
