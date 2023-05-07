# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from filtering import get_recommendations
from score import *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
proba = 0
while (proba < 4) :
    tytul = input()
    print(get_recommendations(tytul))
    proba = proba + 1

#score()
#datafile()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
