import streamlit as st
import pandas as pd
import os
from recommender import recommend

# -------- CONFIG --------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -------- LOAD DATA --------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
movies = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'movies.csv'))

# -------- CUSTOM CSS --------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #00ffe1;
}
.subtitle {
    text-align: center;
    color: #cfcfcf;
    margin-bottom: 30px;
}
.card {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 15px;
    margin: 10px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
}
</style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown('<div class="title">🎬 Movie → Product Recommender</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered smart recommendations</div>', unsafe_allow_html=True)

# -------- SEARCH BAR --------
movie = st.selectbox("🔍 Search or Select a Movie", movies['title'])

# -------- BUTTON --------
if st.button("🚀 Get Recommendations"):
    
    results = recommend(movie)

    st.markdown("## 🛍️ Recommended Products")

    cols = st.columns(3)

    for i, product in enumerate(results):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <h4>{product}</h4>
                <p>⭐ Recommended for you</p>
            </div>
            """, unsafe_allow_html=True)

# -------- FOOTER --------
st.markdown("---")
st.markdown(
    "<center>Built with ❤️ using AI | Streamlit App</center>",
    unsafe_allow_html=True
)