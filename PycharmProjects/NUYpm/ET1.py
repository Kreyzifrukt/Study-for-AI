import pandas as pd
import numpy as np

# 1. Зчитування даних
df = pd.read_csv("transactions.csv")

# Очікувана структура:
# date, category, amount
df['date'] = pd.to_datetime(df['date'])

# 2. Групування витрат по категоріях
category_sum = df.groupby('category')['amount'].sum()
print("Витрати по категоріях:\n", category_sum, "\n")

# 3. Середній чек (NumPy)
avg_check = np.mean(df['amount'])
print("Середній чек:", avg_check, "\n")

# 4. Найдорожчий день тижня
df['weekday'] = df['date'].dt.day_name()
weekday_sum = df.groupby('weekday')['amount'].sum()

most_expensive_day = weekday_sum.idxmax()
print("Найдорожчий день:", most_expensive_day, "\n")

# 5. Прогноз залишку грошей
daily_spending = df.groupby(df['date'].dt.date)['amount'].sum()

avg_daily = np.mean(daily_spending)

days_in_month = 30
days_passed = len(daily_spending)
days_left = days_in_month - days_passed

predicted_future_spending = avg_daily * days_left

current_spent = df['amount'].sum()
budget = 30000  # наприклад бюджет

money_left = budget - (current_spent + predicted_future_spending)

print("Прогноз витрат до кінця місяця:", predicted_future_spending)
print("Очікуваний залишок:", money_left)