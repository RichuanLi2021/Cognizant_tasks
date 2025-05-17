def update_dict_and_print(my_dict):
    my_dict["favorite color"] = "Blue"
    the_keys = []
    the_values = []
    for keys, values in my_dict.items():
        the_keys.append(keys)
        the_values.append(str(values))

    print(f"Keys: " + ", ".join(the_keys))
    print(f"Values: " + ", ".join(the_values))

def main():
    my_info = {
        "name": "Karl Li",
        "age": 28,
        "city": "Halifax"
    }
    update_dict_and_print(my_info)

if __name__ == "__main__":
     main()