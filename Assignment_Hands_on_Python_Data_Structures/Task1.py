"""
    Create a list of your favorite fruits. Add at least five fruits to the list.
        Perform the following operations:
            1. Append a new fruit to the list.
            2. Remove one fruit from the list using the remove() method.
            3. Print the list in reverse order using slicing.
"""

def add_fruits(the_list):
    the_list.append('fig')
    return the_list

def remove_fruits(the_list):
    the_list.remove('apple')
    return the_list

def main():
    original_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f"Original list: {original_list} \n")
    after_added = add_fruits(original_list)
    after_removed = remove_fruits(after_added)
    print(f"""After adding a fruit: {after_added} \n
After removing a fruit: {after_removed} \n
Reversed list: {after_removed[::-1]}
""")


if __name__ == "__main__":
    main()