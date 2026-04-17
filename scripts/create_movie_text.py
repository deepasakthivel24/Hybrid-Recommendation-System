import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

movies_path = os.path.join(BASE_DIR, 'data', 'processed', 'movies.csv')

movies = pd.read_csv(movies_path)

movies['description'] = movies['title'] + " " + movies['genre']

movies.to_csv(movies_path, index=False)

print("✅ Movie descriptions created")