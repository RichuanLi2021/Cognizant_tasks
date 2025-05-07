# Task1_Approach 1: Passing parameters to function to get output.
name = "Karl Li"
age = 28
height = 5.8

def greeting_to_cognizant_externship(ppl_name, ppl_age, ppl_height):
    print(
        f"Hey there! my name is {ppl_name}"
          + f"! I am {ppl_age} years old"
          + f" and I am {ppl_height} feet tall."
        )

greeting_to_cognizant_externship(name,age,height)

# Task1_Approach 2: Dynamic output: Function + List + While loop
my_info = [
    f"Hey there, my name is {name}",
    f"I am {age} years old",
    f"I am {height} feet tall."
]

def greeting_to_cognizant_externship_2(ppl_info):
    # first print the very first item in the list which is index 0
    greeting_messages = ""
    list_length = len(ppl_info)
    if len(ppl_info) == 0:
        print("No information is found")
    else:
        greeting_messages += ppl_info[0]

    # link the rest of items to the message
    # first to check if we have reached the last item in the list or not
    item = 1
    while item < list_length:
        if item == list_length - 1:
            greeting_messages += f" and {ppl_info[item]}"
        else:
            greeting_messages += f", {ppl_info[item]}"
        item += 1

    print(greeting_messages)

greeting_to_cognizant_externship_2(my_info)




