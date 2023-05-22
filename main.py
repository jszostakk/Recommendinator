# This is a sample Python script.
import random
import re

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from filtering import get_recommendations, get_five_posters
from score import *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_five_movies(tytul):
    #proba = 0

    titles = []
    movies = get_recommendations(tytul).head(5)
    for movie in movies:
        titles.append(movie)
    # for movie in movies:
    #     titles.append(movie.to_string(index=False))
    #     print(movie)
    #     print(type(movie))
    # print("Hej" + movies)

    # while (proba < 10):
    #     #tytul = input()
    #     #print(get_recommendations(tytul))
    #     datap = get_recommendations(tytul)
    #
    #     titles.append(datap.values)
    #
    #     proba = proba + 1
    # result = []
    # for i in range(10):
    #     result.append(titles[1][i])
    # print(result[1])
    return titles

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

posters = get_five_posters(["Shrek", "Shrek Forever", "The Adventures of Rocky & Bullwinkle"])
#print(posters[2])
#print(type(posters[2]))
# print(type(get_recommendations("Shrek")))
get_five_movies("Shrek")
#score()
#datafile()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
