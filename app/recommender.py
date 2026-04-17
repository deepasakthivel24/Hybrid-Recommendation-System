import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

movies = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'movies.csv'))
products = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'products.csv'))
mapping = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'movie_product_map.csv'))

def recommend(movie_name):
    movie_id = movies[movies['title'] == movie_name]['movie_id'].values[0]

    product_ids = mapping[mapping['movie_id'] == movie_id]['product_id']

    results = products[products['product_id'].isin(product_ids)]

    return results['product_name'].tolist()