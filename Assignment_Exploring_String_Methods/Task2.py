def scru(strs: str):
   result = \
    (strs
     .strip()
     .capitalize()
     .replace("world", "universe")
     .upper()
     )
   print(result)

def main():
    value = " hello, python world! "
    scru(value)

if __name__ == "__main__":
    main()
