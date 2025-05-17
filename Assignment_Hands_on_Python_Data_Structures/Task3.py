def main():
    the_tuple = ("Attack On Titan", "Counting Star", "Harry Potter")
    msg = ""
    try:
        the_tuple[0] = "Bleach"
    except TypeError as e:
        msg = str(e)
        print(f"Oops! Tuples cannot be changed: {msg}")

    print("Length of tuple: ", len(the_tuple))

if __name__ == "__main__":
    main()