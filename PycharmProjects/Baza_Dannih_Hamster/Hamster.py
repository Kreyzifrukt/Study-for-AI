import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# === База данных ===
def create_database():
    conn = sqlite3.connect("hamsters.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hamsters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            color TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_hamster(name, weight, color, price):
    conn = sqlite3.connect("hamsters.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hamsters (name, weight, color, price) VALUES (?, ?, ?, ?)",
                   (name, weight, color, price))
    conn.commit()
    conn.close()

def get_all_hamsters():
    conn = sqlite3.connect("hamsters.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hamsters")
    rows = cursor.fetchall()
    conn.close()
    return rows

# === Интерфейс ===
def add_hamster():
    name = name_entry.get()
    weight = weight_entry.get()
    color = color_entry.get()
    price = price_entry.get()

    # Проверка на пустые поля
    if not name or not weight or not color or not price:
        messagebox.showwarning("Помилка", "Заповніть всі поля!")
        return

    try:
        insert_hamster(name, float(weight), color, float(price))
        update_table()
        clear_form()
    except ValueError:
        messagebox.showerror("Помилка", "Вага та ціна мають бути числами!")

def update_table():
    for row in tree.get_children():
        tree.delete(row)
    for hamster in get_all_hamsters():
        tree.insert("", tk.END, values=hamster)

def clear_form():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    color_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

# === Главное окно ===
create_database()

root = tk.Tk()
root.title("База Даних Хом'ячків")
root.geometry("600x400")

# === Форма ввода ===
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Ім'я:").grid(row=0, column=0)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Вага (г):").grid(row=1, column=0)
weight_entry = tk.Entry(form_frame)
weight_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Колір:").grid(row=2, column=0)
color_entry = tk.Entry(form_frame)
color_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Вартість (грн):").grid(row=3, column=0)
price_entry = tk.Entry(form_frame)
price_entry.grid(row=3, column=1)

add_button = tk.Button(form_frame, text="Додати хом'ячка", command=add_hamster)
add_button.grid(row=4, column=0, columnspan=2, pady=10)

# === Таблица вывода ===
tree = ttk.Treeview(root, columns=("ID", "Ім'я", "Вага", "Колір", "Ціна"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Ім'я", text="Ім'я")
tree.heading("Вага", text="Вага (г)")
tree.heading("Колір", text="Колір")
tree.heading("Ціна", text="Вартість (грн)")
tree.pack(fill=tk.BOTH, expand=True)

update_table()

root.mainloop()
