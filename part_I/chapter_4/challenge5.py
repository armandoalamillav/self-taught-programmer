def string_convert(s):
    try:
        result = float(s)
        print(result)
    except ValueError:
        print("I need a number")


x = input("Give me some input: ")

y = string_convert(x)