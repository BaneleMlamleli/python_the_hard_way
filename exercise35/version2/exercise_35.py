"""
Fixed syntax error and some small bugs.
I also added the CamelCase package with the CamelCase module for demonstrating package management through pipenv
"""
from sys import exit
from camelcase import CamelCase

c = CamelCase()


def gold_room():
    print(c.hump("This room is full of gold. How much do you take?"))

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print(c.hump("Nice, you're not greedy, you win!"))
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print(c.hump("There is a bear here."))
    print(c.hump("The bear has a bunch of honey."))
    print(c.hump("The fat bear is in front of another door."))
    bear_moved = False
    while True:
        print(
            "How are you going to move the bear(Enter 'H' to Take honey, 'T' to Taunt Bear, 'O' to Open Door)?"
        )
        choice = input("> ")
        if choice[0].lower() == "h":
            dead("The bear looks at you then slaps your face off.")
        elif choice[0].lower() == "t" and (not bear_moved):
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice[0].lower() == "t" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice[0].lower() == "o" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee(F) for your life or eat(E) your head?")
    choice = input("> ")
    if "f" in choice:
        start()
    elif "e" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print(c.hump("you are in a dark room."))
    print(c.hump("There is a door to your right(R) and left(L)."))
    print(c.hump("Which one do you take?"))
    choice = input("> ")
    if choice[0].lower() == "l":
        bear_room()
    elif choice[0].lower() == "r":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
