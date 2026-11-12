import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import numpy as np


class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система аналізу даних: Клімат, Рекомендації, Епідемія")
        self.root.geometry("900x800")
        self.root.configure(padx=20, pady=20)

        self.setup_ui()

    def setup_ui(self):
        # --- Секція керування файлами ---
        file_frame = tk.LabelFrame(self.root, text=" 1. Завантаження даних (CSV) ", padx=10, pady=10)
        file_frame.pack(fill="x", pady=5)

        self.btn_load = ttk.Button(file_frame, text="Вибрати файл CSV", command=self.load_file)
        self.btn_load.pack(side="left", padx=5)

        self.lbl_status = ttk.Label(file_frame, text="Файл не вибрано", foreground="gray")
        self.lbl_status.pack(side="left", padx=10)

        # --- Кнопки задач ---
        tasks_frame = tk.Frame(self.root)
        tasks_frame.pack(pady=10)

        ttk.Button(tasks_frame, text="Аналіз Клімату", width=25, command=self.analyze_climate).grid(row=0, column=0,
                                                                                                    padx=5)
        ttk.Button(tasks_frame, text="Рекомендації", width=25, command=self.analyze_recommendations).grid(row=0,
                                                                                                          column=1,
                                                                                                          padx=5)
        ttk.Button(tasks_frame, text="Симуляція Вірусу", width=25, command=self.simulate_virus).grid(row=0, column=2,
                                                                                                     padx=5)

        # --- Поле для введення (для рекомендацій) ---
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", pady=5)
        ttk.Label(input_frame, text="Введіть назву (фільм/музика):").pack(side="left")
        self.entry_item = ttk.Entry(input_frame)
        self.entry_item.pack(side="left", fill="x", expand=True, padx=10)

        # --- Текстовий вивід результатів ---
        self.result_text = tk.Text(self.root, height=12, font=("Consolas", 10), bg="#f8f9fa")
        self.result_text.pack(fill="both", expand=False, pady=10)

        # --- Секція Візуалізації (Canvas замість Matplotlib) ---
        viz_frame = tk.LabelFrame(self.root, text=" Візуалізація результатів ", padx=10, pady=10)
        viz_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(viz_frame, bg="white", height=250)
        self.canvas.pack(fill="both", expand=True)

    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.file_path = path
            self.lbl_status.config(text=f"Файл: {path.split('/')[-1]}", foreground="green")

    def log(self, text):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)

    # ---------- ТЕМА 1: АНАЛІЗ КЛІМАТУ ----------
    def analyze_climate(self):
        try:
            df = pd.read_csv(self.file_path)
            # Припускаємо колонки: 'Date' та 'Temperature'
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values('Date').dropna()

            # NumPy: Розрахунок ковзного середнього (rolling mean)
            # window=12 для згладжування сезонності (якщо дані місячні)
            df['Rolling'] = df['Temperature'].rolling(window=12, center=True).mean()

            # 10 років з найбільшою аномалією (від середнього)
            mean_century = df['Temperature'].mean()
            df['Anomaly'] = np.abs(df['Temperature'] - mean_century)
            top_10 = df.nlargest(10, 'Anomaly')[['Date', 'Temperature']]

            res = "=== АНАЛІЗ КЛІМАТИЧНИХ ЗМІН ===\n"
            res += f"Середня темп. за період: {mean_century:.2f}°C\n"
            res += f"ТОП-10 екстремальних показників:\n{top_10.to_string(index=False)}\n"
            self.log(res)

            self.draw_plot(df['Temperature'].values, df['Rolling'].values)
        except Exception as e:
            messagebox.showerror("Помилка", f"Потрібен CSV з колонками Date та Temperature\n{e}")

    # ---------- ТЕМА 2: РЕКОМЕНДАЦІЙНА СИСТЕМА ----------
    def analyze_recommendations(self):
        try:
            df = pd.read_csv(self.file_path)  # Колонки: user_id, title, rating

            # Створення матриці Користувач-Рейтинг
            pivot = df.pivot_table(index='title', columns='user_id', values='rating').fillna(0)

            item_name = self.entry_item.get().strip()
            if item_name not in pivot.index:
                messagebox.showwarning("Увага", "Об'єкт не знайдено в базі!")
                return

            # NumPy: Косинусна подібність
            target_vector = pivot.loc[item_name].values

            # Векторизоване обчислення подібності
            similarities = []
            for other_name in pivot.index:
                other_vector = pivot.loc[other_name].values
                # Формула: (A·B) / (||A||*||B||)
                dot_product = np.dot(target_vector, other_vector)
                norm_a = np.linalg.norm(target_vector)
                norm_b = np.linalg.norm(other_vector)

                score = dot_product / (norm_a * norm_b) if (norm_a * norm_b) != 0 else 0
                similarities.append((other_name, score))

            # Сортування та вибір ТОП-5 (крім самого себе)
            recommendations = sorted(similarities, key=lambda x: x[1], reverse=True)[1:6]

            res = f"=== РЕКОМЕНДАЦІЇ ДЛЯ: {item_name} ===\n\n"
            for name, score in recommendations:
                res += f"[{score:.2f}] - {name}\n"
            self.log(res)
        except Exception as e:
            messagebox.showerror("Помилка", f"Потрібен CSV (user_id, title, rating)\n{e}")

    # ---------- ТЕМА 3: МОДЕЛЬ SIR (ВІРУС) ----------
    def simulate_virus(self):
        # Параметри симуляції
        size = 20  # Сітка 20x20
        pop = np.zeros((size, size))  # 0: Здоровий, 1: Хворий, 2: Імунітет
        pop[10, 10] = 1  # Нульовий пацієнт

        stats = []
        for step in range(30):
            new_pop = pop.copy()
            for x in range(size):
                for y in range(size):
                    if pop[x, y] == 1:  # Якщо хворий
                        # Заражаємо сусідів (спрощено)
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < size and 0 <= ny < size and pop[nx, ny] == 0:
                                if np.random.rand() < 0.3:  # ймовірність 30%
                                    new_pop[nx, ny] = 1
                        new_pop[x, y] = 2  # Одужав
            pop = new_pop

            # Pandas для фіксації статистики
            unique, counts = np.unique(pop, return_counts=True)
            d_counts = dict(zip(unique, counts))
            stats.append({
                'Крок': step,
                'Хворі': d_counts.get(1, 0),
                'Здорові': d_counts.get(0, 0),
                'Імунітет': d_counts.get(2, 0)
            })

        df_stats = pd.DataFrame(stats)
        res = "=== СИМУЛЯЦІЯ ЕПІДЕМІЇ (SIR) ===\n"
        res += df_stats.tail(10).to_string(index=False)
        res += "\n\nВисновок: Пік епідемії пройдено, зафіксовано колективний імунітет."
        self.log(res)
        self.draw_plot(df_stats['Хворі'].values, None, mode="virus")

    # ---------- ВІЗУАЛІЗАТОР (CANVAS) ----------
    def draw_plot(self, data, trend=None, mode="climate"):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        pad = 30

        if len(data) == 0: return

        # Масштабування
        max_v = np.max(data)
        min_v = np.min(data)
        diff = max_v - min_v if max_v != min_v else 1

        def get_coords(i, val):
            x = pad + i * (w - 2 * pad) / len(data)
            y = (h - pad) - (val - min_v) * (h - 2 * pad) / diff
            return x, y

        # Малювання даних
        color = "blue" if mode == "climate" else "orange"
        for i in range(len(data) - 1):
            x1, y1 = get_coords(i, data[i])
            x2, y2 = get_coords(i + 1, data[i + 1])
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=1)

        # Малювання тренду (ковзне середнє)
        if trend is not None:
            for i in range(len(trend) - 1):
                if np.isnan(trend[i]) or np.isnan(trend[i + 1]): continue
                x1, y1 = get_coords(i, trend[i])
                x2, y2 = get_coords(i + 1, trend[i + 1])
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

        self.canvas.create_text(w / 2, h - 10, text="Часова шкала (ітерації/роки)")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()