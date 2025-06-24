from array import ArrayType


# Approach 1: Simple method override
# def describe_pet(pet_name: str, animal_type: str = "dog") -> None:
#     print(f"I have a {animal_type} named {pet_name}.")
#
# def main():
#     describe_pet("Buddy")
#     describe_pet("Whiskers", "cat")
#
# if __name__ == "__main__":
#     main()

# Approach 2: Simple recursion
import array
import numbers

def describe_pet(pets: array, index = 0):
    if index == len(pets):
        return
    ani_name, kind = pets[index]
    end_char = ' ' if index < len(pets) - 1 else ''
    message = f"I have a {kind} named {ani_name}. "
    print(message, end=end_char)
    describe_pet(pets, index+1)

def main():
    pets_list = [("Buddy", "dog"), ("Whiskers", "cat")]
    describe_pet(pets_list)

if __name__ == "__main__":
    main()