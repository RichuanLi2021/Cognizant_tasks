# Writing Functions
import numbers

def greet_user(name: str):
    return name

def add_numbers(n1: numbers, n2: numbers):
    return n1 + n2

def main():
    number1 = 5
    number2 = 10
    print(greet_user(f"Hello, Alice! Welcome aboard. The sum of {number1} and {number2} is {add_numbers(number1, number2)}."))

if __name__ == "__main__":
    main()
