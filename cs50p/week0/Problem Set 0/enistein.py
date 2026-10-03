

#main function
def main():
    light_Speed = int(300000000)
    usr_Input = int(input("m: "))
    energy = usr_Input*pow(light_Speed,2)

    print(f"E: {energy}")

main()