"""
    1. Create a string variable with the value "Python is amazing!".
    2. Extract the following using slicing:
        The first 6 characters ("Python")
        The word "amazing"
        The entire string in reverse order
    3. Print each of these slices with a clear label.

    First word: Python
    Amazing part: amazing
    Reversed string: !gnizama si nohtyP
"""

"""
    1. def string_slicing
    2. main()
"""

def string_slicing(strs: str):
    print(f"""
    First word: {strs[0:6]}
    Amazing part: {strs[10:]}
    Reversed string: {strs[::-1]}
""")

def main():
    string_slicing("Python is amazing!")

if __name__ == "__main__":
    main()
