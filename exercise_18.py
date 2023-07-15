# creating a function that will add 2 numbers
def addition(arg1, arg2):
    print(f"Sum: {arg1} + {arg2} = {arg1+arg2}")


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothing.")


addition(3, 7)
print_two("Banele", "Mlamleli")
print_two_again("Shaun", "Tania")
print_one("First arg")
print_none()
