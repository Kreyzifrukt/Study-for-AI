import sqlite3

def create():
    conn = sqlite3.connect("animals.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS animal_types (
        type_id INTEGER PRIMARY KEY AUTOINCREMENT,
        breed TEXT NOT NULL,
        class TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS animals (
        animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        weight REAL,
        height REAL,
        color TEXT,
        type_id INTEGER,
        FOREIGN KEY (type_id) REFERENCES animal_types(type_id)
    )''')

    conn.commit()
    conn.close()

def add_animal_type(breed, animal_class):
    conn = sqlite3.connect("animals.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animal_types (breed, class) VALUES (?, ?)", (breed, animal_class))
    conn.commit()
    conn.close()

def add_animal(name, weight, height, color, type_id):
    conn = sqlite3.connect("animals.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animals (name, weight, height, color, type_id) VALUES (?, ?, ?, ?, ?)",
                   (name, weight, height, color, type_id))
    conn.commit()
    conn.close()

def get_animals_with_types():
    conn = sqlite3.connect("animals.db")
    cursor = conn.cursor()
    cursor.execute('''
    SELECT animals.name AS animal, animals.weight, animals.height, animals.color, 
           animal_types.breed AS breed, animal_types.class
    FROM animals 
    JOIN animal_types ON animals.type_id = animal_types.type_id
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    create()

    add_animal_type("Кіт", "Савець")
    add_animal_type("Собака", "Савець")
    add_animal_type("Комар", "Комаха")

    add_animal("Барсик", 4.5, 30, "Gray", 1)
    add_animal("Дружок", 20.0, 60, "Brown", 2)
    add_animal("Бж", 0.1, 0.1, "Black", 3)

    animals_data = get_animals_with_types()
    for row in animals_data:
        print(
            f"Animal: {row[0]}\tWeight: {row[1]} kg\tHeight: {row[2]} cm\tColor: {row[3]}\tType: {row[4]}\tClass: {row[5]}")
