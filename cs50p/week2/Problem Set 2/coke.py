def main():
    amount_due = 50
    while amount_due >0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert coin: "))
        match coin:
            case 25 | 10 | 5:
                amount_due = amount_due - coin
        
    print(f"Change Owe: {amount_due*-1}")     

main()