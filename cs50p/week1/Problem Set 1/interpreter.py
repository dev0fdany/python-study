def main():
    x , y , z = input("Expression: ").split(" ")
    x = float(x)
    z = float(z)

    check(x,y,z)

def check(x,y,z):
        if y == "+":
            print(x+z)
        elif y == "-":
            print(x-z)
        elif y == "*":
            print(x*z)
        elif y == "/":
            if(z == 0):
                print("Cannot Divide by 0.")
                exit()
            else:
                print(x/z)
        else:
            print("Syntax Error.")
main() 