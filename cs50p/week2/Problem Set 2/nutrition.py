def main():
    item = str(input("Item: "))
    calories = check_calories(item)
    print(f"Calories: {calories}")

def check_calories(n):
    match n.lower():
        case "apple":
            return 130
        case "banana":
            return 110
        case "pear" | "sweet cherries":
            return 100
        case "grapes" | "kiwifruit":
            return 90
        case "orange" | "watermelon":
            return 80
        case "plums":
            return 70
        case "grapfruit" | "nectarine" | "peach":
            return 60
        case "avocado" | "cantaloupe" | "honeydrew melon" | "pineapple" | "strawberries" | "tangerine":
            return 50
        case "lime":
            return 20
        case "lemon":
            return 15

if __name__ == "__main__":
    main()