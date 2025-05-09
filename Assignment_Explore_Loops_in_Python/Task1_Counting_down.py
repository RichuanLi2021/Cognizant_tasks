def get_positive_int(prompt) -> int:
    while True:
        starting_number = input(prompt).strip()
        try:
            n = int(starting_number)
        except ValueError:
            print(f" --> '{starting_number}' Invalid Input.")
        else:
            if n >= 1:
                return n
            print("Number must be ≥ 1.")

def countdown(num: int) -> None:
    for i in range(num, 0, -1):
        print(i, end=' ')
    print("Blast off! 🚀")

def main():
    while True:
        start = get_positive_int("Enter the starting number: ")
        countdown(start)

        again = input("Continue or Exit? (Y/N): ").strip().upper()
        print()
        if again != 'Y':
            print("Seeya!")
            break

# Set a guard to make sure it wont run as being imported elsewhere
if __name__ == "__main__":
    main()