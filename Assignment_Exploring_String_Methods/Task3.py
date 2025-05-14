def palindrome(strs: str):
    reverse = strs[::-1]
    if strs == reverse:
        print(f"Yes, '{strs}' is a palindrome!")
    else:
        print(f"No, '{strs}' is not a palindrome!")

def input_checker(prompt: str):
    while True:
        word = input(prompt).strip()
        if word.isalpha():
            return word
        print(f" → {word} is invalid input: please enter only letters (no digits or symbols).")

def yes_or_no(prompt: str) -> bool:
    while True:
        again = input(prompt).strip().upper()
        if again == 'Y':
            return True
        elif again == 'N':
            return False
        else:
            print("Invalid Input, try again!")

def main():
    while True:
        valid_str = input_checker("Enter a word: ")
        palindrome(valid_str)

        if yes_or_no("Enter 'Y' to continue or 'N' to exit: "):
            continue
        else:
            break

if __name__ == "__main__":
    main()