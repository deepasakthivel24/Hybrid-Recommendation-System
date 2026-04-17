import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
movies_path = os.path.join(BASE_DIR, 'data', 'raw', 'movies.csv')
ratings_path = os.path.join(BASE_DIR, 'data', 'raw', 'ratings.csv')
products_path = os.path.join(BASE_DIR, 'data', 'raw', 'amazon_products.json')

# -------- MOVIES --------
movies = pd.read_csv(movies_path)
ratings = pd.read_csv(ratings_path)

movies = movies[['movieId', 'title', 'genres']]
movies.columns = ['movie_id', 'title', 'genre']

ratings = ratings[['userId', 'movieId', 'rating']]
ratings.columns = ['user_id', 'movie_id', 'rating']

# -------- PRODUCTS --------
products = []

with open(products_path, encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if 'title' in data:
            products.append({
                'product_name': data['title'],
                'category': str(data.get('category', '')),
                'description': data.get('description', '')
            })

products = pd.DataFrame(products)
products['product_id'] = range(1, len(products)+1)

# -------- SAVE --------
processed_dir = os.path.join(BASE_DIR, 'data', 'processed')

movies.to_csv(os.path.join(processed_dir, 'movies.csv'), index=False)
ratings.to_csv(os.path.join(processed_dir, 'ratings.csv'), index=False)
products.to_csv(os.path.join(processed_dir, 'products.csv'), index=False)

print("✅ Data preprocessing completed")