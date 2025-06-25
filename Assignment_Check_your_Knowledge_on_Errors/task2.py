import void

def type_error(name: str, num: int) -> None:
    try:
        print(name + num)
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

def key_error(dic: dict[str, int] | None = None) -> None:
    if dic is None:
        print("No dictionary provided")
    key: str = "C"
    try:
        value = dic[key]
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

def index_error(lis: list[int] | None = None) -> None:
    if lis is None:
        print("you have to pass a valid list")
        return
    out_of_index = len(lis)
    try:
        value: int = lis[out_of_index]
    except IndexError:
        print("IndexError occurred! List index out of range.")


def main():
    index_list = [1, 2, 3, 4]
    index_error(index_list)

    key_dic: dict[str, int] = {"A": 1, "B": 2}
    key_error(key_dic)

    name: str = "karl"
    age: int = 22
    type_error(name, age)
    return

if __name__ == "__main__":
    main()