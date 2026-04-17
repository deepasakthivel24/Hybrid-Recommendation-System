import pandas as pd
import pickle
import os
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

movies = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'movies.csv'))
products = pd.read_csv(os.path.join(BASE_DIR, 'data', 'processed', 'products.csv'))

model = SentenceTransformer('all-MiniLM-L6-v2')

# Movie embeddings
movies['embedding'] = movies['description'].apply(lambda x: model.encode(x))

# Product embeddings
products['text'] = products['product_name'] + " " + products['category']
products['embedding'] = products['text'].apply(lambda x: model.encode(x))

# Save
pickle.dump(movies, open(os.path.join(BASE_DIR, 'model', 'movies.pkl'), 'wb'))
pickle.dump(products, open(os.path.join(BASE_DIR, 'model', 'products.pkl'), 'wb'))

print("✅ Embeddings created")