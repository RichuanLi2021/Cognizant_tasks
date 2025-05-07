# Task2 & Task3 - Operators: Playing with Numbers and The Number Checker as a WHOLE
"""
    This is a SMART and SIMPLE Calculator
     - It is SMART because it will tell you what's going wrong if you type something wrong
        and tell you whether the number you entered is positive, negative, or zero
     - It is SIMPLE because it was written in Python (Just kidding)
     - It is my first Calculator built with Python ^_^

     What would I further develop it?
        1. I would create unit testing
        2. I would create a UI for this Calculator so that make it actually a Calculator
        3. I would build a database on its backend to store the history of input and results
        4. I would build API endpoints or both the communication between frontend and backend
        5. I would MAKE IT SOUND whenever it receives inputs. (Sounds very old...)
        6. Yeah, these are just thoughts at this point, not sure if I would really do it. I will see... haha
"""

from Exceptions.A1_Exception import OperationNotFoundError

class Task2Calculator:
    def __init__(self, num1: int, num2: int, arithmetic_operator: str):
        self.num1 = num1
        self.num2 = num2
        self.arithmetic_operator = arithmetic_operator

    def calculate(self):
        match self.arithmetic_operator:
            case "+":
                return self.addition()
            case "-":
                return self.subtraction()
            case "*":
                return self.multiplication()
            case "/":
                return self.division()
            case "%":
                return self.modulus()
            case _:
                raise OperationNotFoundError(f"Invalid operator: ", self.arithmetic_operator)

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2

    def modulus(self):
        return self.num1 % self.num2


def get_int(prompt: str) -> int:
    while True:
        input_int = input(prompt)
        try:
            return int(input_int)
        except ValueError:
            print("Invalid input: Oops, Bro you've gotta double check what you entered.")

def get_operator(prompt: str) -> str:
    operations = {"+", "-", "*", "/", "%"}
    while True:
        input_str = input(prompt)
        if not input_str in operations:
            raise OperationNotFoundError(
                "Invalid operation: Oops, you have to start again...",
                input_str
            )
        return input_str

def number_checker(number: int):
    if number == 0:
        print("Zero it is. A perfect balance!\n")
    elif number > 0:
        print("This number is positive. Awesome!\n")
    else:
        print("This number is negative. Better luck next time!\n")

while True:
    firstValue = get_int("Please enter a valid number (e.g. 10): ")
    number_checker(firstValue)
    operator = get_operator("Please enter the Arithmetic operator (e.g. + - * / %): ")
    secondValue = get_int("\nPlease enter the second number: ")
    number_checker(secondValue)

    calculator = Task2Calculator(firstValue, secondValue, operator)
    outcome = calculator.calculate()
    print(f"Result: {firstValue} {operator} {secondValue} = {outcome}")

    oneMoreTime = input("It is so boring right? Enter Y if you wanna do it again, otherwise N to exit: ")
    if oneMoreTime != "Y":
        print("You are the first user of my Calculator! Bye~~~~")
        break












