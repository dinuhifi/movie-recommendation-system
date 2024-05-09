import streamlit as st
import pickle as pk
import pandas as pd
import requests
from config import API_KEY

with open('movies.pkl', 'rb') as file:
    movies = pk.load(file)
with open('df1.pkl', 'rb') as file:
    content_based_df = pd.DataFrame(pk.load(file))
with open('similarity.pkl', 'rb') as file:
    similarity = pk.load(file)

def content_based_recommend(movie):
    index = content_based_df[content_based_df["title"] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    L = []
    for i in movies_list:
        L.append(content_based_df.iloc[i[0]].title)
    return L

def get_poster_url(movie):
    url = "http://www.omdbapi.com/?i="
    imdb_id = content_based_df[content_based_df["title"] == movie]["imdb_id"].values[0]
    url = url+imdb_id+API_KEY
    r = requests.get(url)
    image_path = r.json()
    r.close()
    return image_path["Poster"]

st.title("Movie Recommender System")
chosen_movie = st.selectbox("Choose a Movie you like:", movies)
button = st.button("Recommend!")
if button:
    movie = content_based_recommend(chosen_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader(movie[0])
        poster_url = get_poster_url(movie[0])
        if poster_url:
            st.image(poster_url, caption=movie[0])

    with col2:
        st.subheader(movie[1])
        poster_url = get_poster_url(movie[1])
        if poster_url:
            st.image(poster_url, caption=movie[1])

    with col3:
        st.subheader(movie[2])
        poster_url = get_poster_url(movie[2])
        if poster_url:
            st.image(poster_url, caption=movie[2])

    with col4:
        st.subheader(movie[3])
        poster_url = get_poster_url(movie[3])
        if poster_url:
            st.image(poster_url, caption=movie[3])

    with col5:
        st.subheader(movie[4])
        poster_url = get_poster_url(movie[4])
        if poster_url:
            st.image(poster_url, caption=movie[4])