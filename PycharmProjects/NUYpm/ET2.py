import pandas as pd
import numpy as np

# структура:
# home_team, away_team, home_goals, away_goals
df = pd.read_csv("matches.csv")

# 1. Логіка результатів (NumPy)
home_win = df['home_goals'] > df['away_goals']
draw = df['home_goals'] == df['away_goals']
away_win = df['home_goals'] < df['away_goals']

df['home_points'] = np.where(home_win, 3, np.where(draw, 1, 0))
df['away_points'] = np.where(away_win, 3, np.where(draw, 1, 0))

# 2. Турнірна таблиця
home_table = df.groupby('home_team')['home_points'].sum()
away_table = df.groupby('away_team')['away_points'].sum()

table = home_table.add(away_table, fill_value=0).reset_index()
table.columns = ['team', 'points']

table = table.sort_values(by='points', ascending=False)
print("Турнірна таблиця:\n", table, "\n")

# 3. Середня результативність (NumPy)
total_goals = np.sum(df['home_goals'] + df['away_goals'])
matches = len(df)

avg_goals = total_goals / matches
print("Середня кількість голів за матч:", avg_goals)

# 4. Команда-сюрприз (перемоги проти ТОП-5)
top5 = table.head(5)['team']

surprise = df[
    ((df['home_team'].isin(top5)) & (away_win)) |
    ((df['away_team'].isin(top5)) & (home_win))
]

surprise_teams = pd.concat([
    surprise['home_team'][home_win],
    surprise['away_team'][away_win]
])

print("\nКоманда-сюрприз:\n", surprise_teams.value_counts().head(1))