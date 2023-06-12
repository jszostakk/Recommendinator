from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from ast import literal_eval
import difflib


def datafile():
    datafile1 = pd.read_csv("tmdb_5000_credits.csv")
    datafile2 = pd.read_csv("tmdb_5000_movies.csv")

    datafile1.columns = ['id', 'title', 'cast', 'crew']
    datafile = datafile2.merge(datafile1, on='id')
    return datafile


pd.set_option('display.max_colwidth', None)
datafile = datafile()
fields = ['title', 'backdrop_path']
df = pd.read_csv('movie_data.csv', lineterminator='\n', skipinitialspace=True, usecols=fields)
df.set_index('title')

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
datafile['director_for_getter'] = datafile['crew'].apply(get_director)

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
    else:
        return "Doesn't find this movie, try check the title"

    idx = indices[close_match]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:15]

    movie_indices = [i[0] for i in sim_scores]

    return datafile['title_y'].iloc[movie_indices]


def get_five_movies(tytul):
    titles = []
    movies = get_recommendations(tytul).head(5)
    for movie in movies:
        titles.append(movie)
    return titles


def get_five_posters(movies):
    poster_list = []
    for movie in movies:
        poster_path = df[df['title'].str.match(movie)].head(1).get("backdrop_path").to_string(index=False)
        if poster_path == 'Series([], )':
            poster_list.append(None)
        else:
            poster_list.append(poster_path)
    return poster_list


def get_poster(title):
    poster_path = df[df['title'].str.match(title)].head(1).get("backdrop_path").to_string(index=False)
    if poster_path == 'Series([], )':
        return None
    else:
        return poster_path


def get_director(title):
    if datafile[datafile['title_y'].str.match(title)].head(1).get("director_for_getter").to_string(
            index=False) != "Series([], )":
        return datafile[datafile['title_y'].str.match(title)].head(1).get("director_for_getter").to_string(index=False)
    else:
        return "*Director not found*"


def get_description(title):
    if datafile[datafile['title_y'].str.match(title)].head(1).get("overview").to_string(index=False) != "Series([], )":
        return datafile[datafile['title_y'].str.match(title)].head(1).get("overview").to_string(index=False)
    else:
        return "*Description not found*"
