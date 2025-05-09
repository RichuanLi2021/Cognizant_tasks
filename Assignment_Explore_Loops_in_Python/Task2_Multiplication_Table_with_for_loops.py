"""
    1. Input Checker
    2. Multiplication Table that takes in the input and loop
    3. main function

    Simple output:
    Enter a number: 4
        4 x 1 = 4 4 x 2 = 8 ... 4 x 10 = 40
"""

def multiplication_table(num: int):
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}", end=' ')


def input_checker(prompt: str) -> int:
    while True:
        num = input(prompt).strip()
        try:
            num = int(num)
            return num
        except ValueError:
            print(f" --> '{num}' Invalid input.")


def main():
    valid_num = input_checker("Enter a number: ")
    multiplication_table(valid_num)

if __name__ == "__main__":
    main()
