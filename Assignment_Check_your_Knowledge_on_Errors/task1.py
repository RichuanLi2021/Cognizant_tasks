def division(num: int):
    result = 100 % num
    return result

def input_checker(prompt: str) -> int:
    while True:
        valid_input = input(prompt).strip()
        try:
            value = int(valid_input)
            if value == 0:
                raise ZeroDivisionError("Oops! You cannot divide by zero.")
            else:
                return value
        except ValueError:
            print(f"{valid_input!r} Invalid input! Please enter a valid number.")

def main():
    validated = input_checker("Enter a number: ")
    print(f"100 divided by {validated} is {division(validated)}")
    return

if __name__ == "__main__":
    main()