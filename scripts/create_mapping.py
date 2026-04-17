import pickle
import numpy as np
import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

movies = pickle.load(open(os.path.join(BASE_DIR, 'model', 'movies.pkl'), 'rb'))
products = pickle.load(open(os.path.join(BASE_DIR, 'model', 'products.pkl'), 'rb'))

movie_emb = list(movies['embedding'])
product_emb = list(products['embedding'])

similarity = cosine_similarity(movie_emb, product_emb)

mapping = []

for i in range(len(movies)):
    top_products = np.argsort(similarity[i])[-3:]

    for p in top_products:
        mapping.append({
            'movie_id': movies.iloc[i]['movie_id'],
            'product_id': products.iloc[p]['product_id']
        })

mapping_df = pd.DataFrame(mapping)

mapping_df.to_csv(os.path.join(BASE_DIR, 'data', 'processed', 'movie_product_map.csv'), index=False)

print("✅ Mapping created")