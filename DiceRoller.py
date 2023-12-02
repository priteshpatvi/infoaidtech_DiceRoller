import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        # Simulate rolling a single die (random number between 1 and 6)
        result = random.randint(1, 6)
        results.append(result)
    return results

def main():
    print("Welcome to the Dice Rolling App!")

    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? (Enter 0 to quit): "))

            if num_dice < 0:
                print("Please enter a positive number or 0 to quit.")
                continue

            if num_dice == 0:
                print("Goodbye!")
                break

            dice_results = roll_dice(num_dice)
            print(f"Result{'s' if num_dice > 1 else ''}: {', '.join(map(str, dice_results))}")

        except ValueError:
            print("Invalid input. Please enter a positive number or 0 to quit.")

if __name__ == "__main__":
    main()
