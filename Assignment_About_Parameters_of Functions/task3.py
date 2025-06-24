import numbers

def make_sandwich(*num_ingredients):

    if not num_ingredients:
        print("No ingredients provided.")
        return

    ingredients = ""
    for item in num_ingredients:
        ingredients = ingredients + f" - {item}"
    print(f"Making a sandwich with the following ingredients: {ingredients}")


def main():
    return make_sandwich("Lettuce", "Tomato", "Cheese")

if __name__ == "__main__":
    main()