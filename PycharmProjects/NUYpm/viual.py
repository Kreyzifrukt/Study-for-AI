import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np


# ---------------------- ФУНКЦІЇ ----------------------

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV файли", "*.csv")])
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)


def clear_output():
    result_text.delete(1.0, tk.END)


# ---------- ТЕМА 1: АНАЛІЗАТОР ФІНАНСІВ ----------
def analyze_finance():
    try:
        path = entry_file.get()
        df = pd.read_csv(path)
        df['date'] = pd.to_datetime(df['date'])

        clear_output()

        # Групування за категоріями (Pandas)
        category_sum = df.groupby('category')['amount'].sum()

        # Розрахунок середнього чека (NumPy)
        avg_check = np.mean(df['amount'].values)

        # Найдорожчий день тижня
        df['weekday'] = df['date'].dt.day_name()
        days_ua = {
            'Monday': 'Понеділок', 'Tuesday': 'Вівторок', 'Wednesday': 'Середа',
            'Thursday': 'Четвер', 'Friday': "П'ятниця", 'Saturday': 'Субота', 'Sunday': 'Неділя'
        }
        expensive_day_en = df.groupby('weekday')['amount'].sum().idxmax()
        expensive_day = days_ua.get(expensive_day_en, expensive_day_en)

        # Прогноз до кінця місяця (NumPy)
        daily_expenses = df.groupby(df['date'].dt.date)['amount'].sum()
        avg_daily = np.mean(daily_expenses.values)

        # Припускаємо 30 днів у місяці
        days_passed = len(daily_expenses)
        predicted_remaining = avg_daily * (30 - days_passed)

        # Вивід результатів
        res = "=== АУДИТ ВИТРАТ (СІМЕЙНИЙ БЮДЖЕТ) ===\n"
        res += f"\nВитрати за категоріями:\n{category_sum.to_string()}\n"
        res += f"\nСередній чек: {avg_check:.2f} грн"
        res += f"\nНайдорожчий день тижня: {expensive_day}"
        res += f"\nПрогноз витрат до кінця місяця: {max(0, predicted_remaining):.2f} грн\n"
        result_text.insert(tk.END, res)

    except Exception as e:
        messagebox.showerror("Помилка", f"Перевірте CSV (потрібні колонки: date, amount, category)\nДеталі: {e}")


# ---------- ТЕМА 2: СПОРТИВНИЙ СКАУТ ----------
def analyze_sport():
    try:
        df = pd.read_csv(entry_file.get())
        clear_output()

        # Нарахування очок через NumPy (3 за перемогу, 1 за нічию)
        df['h_pts'] = np.where(df['home_goals'] > df['away_goals'], 3,
                               np.where(df['home_goals'] == df['away_goals'], 1, 0))
        df['a_pts'] = np.where(df['away_goals'] > df['home_goals'], 3,
                               np.where(df['home_goals'] == df['away_goals'], 1, 0))

        # Створення турнірної таблиці
        t1 = df.groupby('home_team')['h_pts'].sum()
        t2 = df.groupby('away_team')['a_pts'].sum()
        standings = t1.add(t2, fill_value=0).sort_values(ascending=False).reset_index()
        standings.columns = ['Команда', 'Очки']

        # Команда-сюрприз (перемоги над ТОП-5)
        top_5 = standings.head(5)['Команда'].tolist()
        surprise_wins = df[
            ((df['home_team'].isin(top_5) == False) & (df['h_pts'] == 3) & (df['away_team'].isin(top_5))) |
            ((df['away_team'].isin(top_5) == False) & (df['a_pts'] == 3) & (df['home_team'].isin(top_5)))
            ]

        winners = pd.concat([surprise_wins[surprise_wins['h_pts'] == 3]['home_team'],
                             surprise_wins[surprise_wins['a_pts'] == 3]['away_team']])

        surprise_team = winners.value_counts().idxmax() if not winners.empty else "Не визначена"

        # Середня результативність
        avg_goals = np.mean(df['home_goals'] + df['away_goals'])

        res = "=== АНАЛІЗ ФУТБОЛЬНОЇ ЛІГИ ===\n"
        res += f"\nПідсумкова таблиця:\n{standings.to_string(index=False)}\n"
        res += f"\nСередня результативність: {avg_goals:.2f} голів за матч"
        res += f"\nКоманда-сюрприз (перемоги над фаворитами): {surprise_team}\n"
        result_text.insert(tk.END, res)

    except Exception as e:
        messagebox.showerror("Помилка", f"Перевірте CSV (home_team, away_team, home_goals, away_goals)\n{e}")


# ---------- ТЕМА 3: SMART LIBRARY ----------
def analyze_library():
    try:
        df = pd.read_csv(entry_file.get())
        clear_output()

        # Фільтрація: більше 10 оцінок
        movie_stats = df.groupby('title')['rating'].agg(['mean', 'count'])
        popular_items = movie_stats[movie_stats['count'] > 10].sort_values(by='mean', ascending=False)

        # Пошук за жанром та формула популярності
        genre_query = entry_genre.get().strip()
        genre_df = df[df['genre'].str.lower() == genre_query.lower()]

        res = "=== СИСТЕМА РЕКОМЕНДАЦІЙ ===\n"
        res += f"\nТОП-5 за рейтингом (понад 10 оцінок):\n{popular_items['mean'].head(5).to_string()}\n"

        if not genre_df.empty:
            g_stats = genre_df.groupby('title')['rating'].agg(['mean', 'count'])
            # Формула через NumPy: популярність = кількість переглядів + середня оцінка
            g_stats['popularity'] = np.add(g_stats['count'].values, g_stats['mean'].values)
            top_3 = g_stats.sort_values(by='popularity', ascending=False).head(3)
            res += f"\nТОП-3 рекомендації у жанрі '{genre_query}':\n{top_3['popularity'].to_string()}"
        else:
            res += f"\nЖанр '{genre_query}' не знайдено."

        result_text.insert(tk.END, res)

    except Exception as e:
        messagebox.showerror("Помилка", f"Перевірте CSV (title, rating, genre)\n{e}")


# ---------------------- ГРАФІЧНИЙ ІНТЕРФЕЙС (UI) ----------------------

root = tk.Tk()
root.title("Аналізатор Даних (Pandas + NumPy)")
root.geometry("650x650")
root.configure(padx=20, pady=20)

# Вибір файлу
tk.Label(root, text="Шлях до файлу CSV:", font=('Arial', 10, 'bold')).pack(anchor='w')
file_frame = tk.Frame(root)
file_frame.pack(fill='x', pady=5)
entry_file = tk.Entry(file_frame)
entry_file.pack(side='left', fill='x', expand=True, padx=(0, 5))
tk.Button(file_frame, text="Огляд", command=load_file).pack(side='right')

# Поле для жанру
tk.Label(root, text="Введіть жанр (для рекомендацій):", font=('Arial', 10)).pack(anchor='w', pady=(10, 0))
entry_genre = tk.Entry(root)
entry_genre.pack(fill='x', pady=5)

# Кнопки задач
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Аналіз фінансів", width=20, command=analyze_finance).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Спортивний скаут", width=20, command=analyze_sport).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Smart Library", width=20, command=analyze_library).grid(row=0, column=2, padx=5)

# Поле виводу
result_text = tk.Text(root, height=20, font=('Courier New', 10))
result_text.pack(fill='both', expand=True)

root.mainloop()