def input_checker() -> tuple[int, int]:
    while True:
        first_num = input("Enter the first number: ").strip()
        sec_num = input("Enter the second number: ").strip()
        try:
            num1 = int(first_num)
            num2 = int(sec_num)
            return num1, num2
        except ValueError:
            print(f"Invalid input: '{first_num}' or '{sec_num}' is not a number. Please try again.\n")

def main() -> None:
    num1, num2 = input_checker()

    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        # Catches any other unforeseen runtime errors
        print(f"Unexpected error: {e}")
    else:
        # Only runs if no exception was raised above
        print(f"The result is {result}")
    finally:
        # Always runs
        print("This block always executes.")

if __name__ == "__main__":
    main()