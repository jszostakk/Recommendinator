# This is a sample Python script.
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from filtering import get_recommendations
from score import *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_five_movies(tytul):
    proba = 0
    recommendations = []

    while (proba < 20):
        #tytul = input()
        #print(get_recommendations(tytul))
        datap = get_recommendations(tytul)
        recommendations.append(datap)
        # print(datap.head(5))
        proba = proba + 1
    random_sample = random.sample(recommendations, 5)

    return random_sample

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

#score()
#datafile()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
