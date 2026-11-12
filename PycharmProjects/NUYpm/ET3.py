import pandas as pd
import numpy as np

df = pd.read_csv("ratings.csv")

#Статистика по фільмах
stats = df.groupby('movie').agg({
    'rating': ['mean', 'count']
})

stats.columns = ['avg_rating', 'views']

#Фільтрація (>10 оцінок)
filtered = stats[stats['views'] > 10]

top_movies = filtered.sort_values(by='avg_rating', ascending=False)
print("ТОП фільмів:\n", top_movies.head(), "\n")

def recommend(genre):
    subset = df[df['genre'] == genre]

    stats = subset.groupby('movie').agg({
        'rating': ['mean', 'count']
    })

    stats.columns = ['avg_rating', 'views']

    # формула популярності через NumPy
    stats['score'] = np.array(stats['views']) + np.array(stats['avg_rating'])

    return stats.sort_values(by='score', ascending=False).head(3)

print("Рекомендації (Action):\n", recommend("Action"))