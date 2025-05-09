"""
    Task3
    1. Input Checker
    2. Factorial function that takes in input and loop
    3. Main function to execute

    Simple output:
    Enter a number: 5
       n! = n x (n - 1)!
        5! = 5 x 4 x 3 x 2 x 1 = 120
        The factorial of 5 is 120.
"""

## With for loop
def factorial_function(num: int) -> int:
    result = 1
    for i in range(num, 1, -1):
            result *= i
    return result

## With recursion
def factorial_recursion(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial_recursion(n - 1)

def input_checker(prompt: str):
    while True:
        num = input(prompt).strip()
        try:
            n = int(num)
        except ValueError:
            print(f" --> '{num}' is invalid input.")
        else:
            if n >= 0:
                return n
            print("Entered number has to be positive integer! \n")

def main():
    y_n = ["Y", "N"]
    check = True
    while check:
        valid_input = input_checker("Enter a number: ")
        print(f"The factorial of {valid_input} is {factorial_function(valid_input)}. (With for loop)\n")
        print(f"The factorial of {valid_input} is {factorial_recursion(valid_input)}. (With recursion)\n")

        while True:
            again = input("Continue or Exit? (Y/N): ").strip().upper()
            print()

            if again not in y_n:
                print("Cannot recognize the command, try only 'Y' or 'N' \n")
                continue

            elif again != "Y":
                print("Seeya!")
                check = False
                break
            break

if __name__ == "__main__":
    main()