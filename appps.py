import pickle

import pandas as pd
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=3b4a5a0e2515f526e8221350cb4ae73a"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYjRhNWEwZTI1MTVmNTI2ZTgyMjEzNTBjYjRhZTczYSIsInN1YiI6IjY1MDE3NmQxZGI0ZWQ2MTAzODU2NTUwYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ha-xhrUMmnYIhS41RrNGCrmnXgzeoExjzXkFMmP8esI"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    poster_path = data['poster_path']
    return 'https://image.tmdb.org/t/p/w500/' + poster_path

def recommanded(movie):
    index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    rec = []
    rec_poster = []
    for i in movie_list[0:6]:
        id = movies.iloc[i[0]].movie_id
        rec.append(movies.iloc[i[0]].title)
        rec_poster.append(fetch_poster(id))
    return rec, rec_poster


st.header('Movie Recommender System')
movies = pickle.load(open('movie_dict_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommanded(selected_movie)
    post = recommended_movie_posters[0]

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(post)
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




