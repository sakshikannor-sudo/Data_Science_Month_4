import streamlit as st
import pickle
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# =========================
# LOAD MODELS
# =========================

movies = pickle.load(open('../models/movies.pkl', 'rb'))
similarity = pickle.load(open('../models/similarity.pkl', 'rb'))

# =========================
# RECOMMEND FUNCTION
# =========================

def recommend(movie):

    # Find movie index
    movie_index = movies[movies['title'] == movie].index[0]

    # Get similarity scores
    distances = similarity[movie_index]

    # Sort movies based on similarity
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    # Fetch recommended movie names
    for i in movies_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies

# =========================
# UI DESIGN
# =========================

st.title("🎬 Movie Recommendation System")

st.markdown("""
This system recommends movies based on:
- Overview
- Genres
- Keywords
- Cast
- Director
""")

st.divider()

# =========================
# MOVIE SELECTION
# =========================

selected_movie = st.selectbox(
    "Select a Movie",
    movies['title'].values
)

# =========================
# RECOMMEND BUTTON
# =========================

if st.button('Recommend Movies'):

    recommendations = recommend(selected_movie)

    st.subheader("Top 5 Recommended Movies")

    for movie in recommendations:
        st.write("✅", movie)

# =========================
# FOOTER
# =========================

st.divider()

st.caption("Built using Python, Scikit-learn, NLP, and Streamlit")
