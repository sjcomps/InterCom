# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_insult(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'You are such a {name}!')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_insult('Loser')
    benutzereingabe = input("(Do you agree? Y/N) \n")
    if benutzereingabe == "Y":
        print("That's the only thing, that you got right.")
    elif benutzereingabe == "N":
        print("That doesn't change the fact.")
    else:
        print("Your answer will be terminated.")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
