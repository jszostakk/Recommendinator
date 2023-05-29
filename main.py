# This is a sample Python script.
import random
import re

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#from filtering import get_recommendations, get_five_posters
from filtering import *
from score import *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hi! Write down title of the movie : ")

# proba = 0
# recommendations = []
# while (proba < 20) :
#     tytul = input()
#     print(get_recommendations(tytul))
#     datap = get_recommendations(tytul)
#     recommendations.append(datap)
#     #print(datap.head(5))
#     proba = proba + 1

#posters = get_five_posters(["Shrek", "Shrek Forever", "The Adventures of Rocky & Bullwinkle"])
#print(posters[2])
#print(type(posters[2]))
# print(type(get_recommendations("Shrek")))
#get_five_movies("Shrek")
#score()
#datafile()
print(get_director("Shrek"))
print(get_description("Shrek"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
