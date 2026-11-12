import sqlite3

# --- Створення таблиці та додавання даних ---
def create_table_and_insert_data():
    conn = sqlite3.connect("fruits_veggies.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            color TEXT,
            calories INTEGER
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany('''
            INSERT INTO products (name, type, color, calories)
            VALUES (?, ?, ?, ?)
        ''', [
            ("Яблуко", "Фрукт", "Червоний", 52),
            ("Банан", "Фрукт", "Жовтий", 89),
            ("Морква", "Овоч", "Помаранчевий", 41),
            ("Огірок", "Овоч", "Зелений", 16)
        ])
        print("Дані додано в таблицю")
    else:
        print("Таблиця вже містить дані")

    conn.commit()
    conn.close()
def connect_to_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print("Успішно підключено до бази даних")
        return conn
    except Exception as e:
        print("Помилка підключення:", e)
        return None
def disconnect_from_db(conn):
    if conn:
        conn.close()
        print("З'єднання з базою даних закрито.")
def show_all_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    print("\nВся інформація:")
    for row in rows:
        print(row)

def show_all_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM products")
    names = cursor.fetchall()
    print("\nУсі назви:")
    for name in names:
        print(name[0])

def show_all_colors(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT color FROM products")
    colors = cursor.fetchall()
    print("\nУсі кольори:")
    for color in colors:
        print(color[0])

def show_max_calories(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(calories) FROM products")
    print("\nМаксимальна калорійність:", cursor.fetchone()[0])

def show_min_calories(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(calories) FROM products")
    print("\nМінімальна калорійність:", cursor.fetchone()[0])

def show_avg_calories(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(calories) FROM products")
    print("\nСередня калорійність:", round(cursor.fetchone()[0], 2))

create_table_and_insert_data()

conn = connect_to_db("fruits_veggies.db")

if conn:
    show_all_data(conn)
    show_all_names(conn)
    show_all_colors(conn)
    show_max_calories(conn)
    show_min_calories(conn)
    show_avg_calories(conn)
    disconnect_from_db(conn)
