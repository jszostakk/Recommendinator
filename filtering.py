from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from score import datafile
from ast import literal_eval
import difflib


datafile = datafile()

features = ['cast', 'crew', 'keywords', 'genres']
for feature in features:
    datafile[feature] = datafile[feature].apply(literal_eval)

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]

        if len(names) > 3:
            names = names[:3]
        return names


    return []

datafile['director'] = datafile['crew'].apply(get_director)

features = ['cast', 'keywords', 'genres']
for feature in features:
    datafile[feature] = datafile[feature].apply(get_list)

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

features = ['cast', 'keywords', 'director', 'genres']

for feature in features:
    datafile[feature] = datafile[feature].apply(clean_data)

def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])
datafile['soup'] = datafile.apply(create_soup, axis=1)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(datafile['soup'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

datafile = datafile.reset_index()
indices = pd.Series(datafile.index, index=datafile['title_y'])


def get_recommendations(title):
    list_of_all_titles = datafile['title_y'].tolist()
    find_close_match = difflib.get_close_matches(title, list_of_all_titles)
    if find_close_match:
        close_match = find_close_match[0]
        print("Propozycje dla filmu : " + close_match)
    else:
        return "Doesn't find this movie, try check the title"
    # Get index given the title
    idx = indices[close_match]

    # Get similarty score of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    print(sim_scores)

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    print("Sorted sim : " + sim_scores)

    sim_scores = sim_scores[1:15]

    movie_indices = [i[0] for i in sim_scores]

    return datafile['title_y'].iloc[movie_indices]

