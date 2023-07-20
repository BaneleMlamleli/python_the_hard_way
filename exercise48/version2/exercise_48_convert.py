def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


print(convert_number("2"))
