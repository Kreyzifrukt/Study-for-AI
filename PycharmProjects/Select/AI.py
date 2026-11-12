import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#приєднались до БД
def get_connect():
    conn = sqlite3.connect("student.db")
    conn.row_factory = sqlite3.Row
    return conn

#створили таблички у БД
def create_table():
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faculties(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT NOT NULL)""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    ave REAL NOT NULL,
    faculties_id INTEGER NOT NULL,
    FOREIGN KEY(faculties_id) REFERENCES faculties(id))""")
    conn.commit()
    conn.close()

#функція додавання факультета до БД
def insert_faculty(name, code):
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO faculties (name, code) VALUES (?, ?)",
        (name, code)
    )
    conn.commit()
    conn.close()

#функція додавання студента до БД
def insert_student(name, age, ave, faculties_id):
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, ave, faculties_id) VALUES (?, ?, ?, ?)",
        (name, age, ave, faculties_id)
    )
    conn.commit()
    conn.close()

#функція видалення студента із БД по id
def delete_student_by_id(student_id):
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

#функція, яка отримає id студента із html форми
#та запустить функцію видалення студента
#із БД по id
@app.route('/delete_student', methods=['POST'])
def delete_student_route():
    student_id = request.form.get('id')
    if student_id:
        delete_student_by_id(student_id)
    return redirect('/')

#функція вичитує та повертає усі факультети із БД
def get_all_faculties():
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM faculties")
    data = cursor.fetchall()
    conn.close()
    return data

#функція, що вичитує студентів (з фільтрацією або без)
#із БД та повертає їх
def get_student_faculties(faculty_name=None):
    conn = get_connect()
    cursor = conn.cursor()
    if faculty_name:
        cursor.execute("""
        SELECT students.*, faculties.name AS faculty_name
        FROM students
        LEFT JOIN faculties ON faculties.id = students.faculties_id
        WHERE faculties.name = ?""", (faculty_name,))
    else:
        cursor.execute("""
        SELECT students.*, faculties.name AS faculty_name
        FROM students
        LEFT JOIN faculties ON faculties.id = students.faculties_id""")
    data = cursor.fetchall()
    conn.close()
    return data

#головна саторінки
@app.route('/')
def index():
    #отримали назву факультета із форми
    faculty_name = request.args.get('faculty')
    #отримали студентів
    students = get_student_faculties(faculty_name)
    #отримали факультети
    faculties = get_all_faculties()
    #відправили цю інформацію на сторінку
    return render_template(
        'index.html',
        students=students,
        faculties=faculties,
        faculty_name=faculty_name
    )

#функція додавання факультета із форми HTML
@app.route('/add_faculty', methods=['POST'])
def add_faculty_route():
    #отримали назву факультета
    name = request.form.get('name')
    #та його шифр
    code = request.form.get('code')
    #якщо вони заповнені
    if name and code:
        #передали дані в функцію додавання факультета
        insert_faculty(name, code)
        #оновлюємо сторніку
    return redirect('/')

#функція додавання студента із форми HTML
@app.route('/add_student', methods=['POST'])
def add_student_route():
    #отримали параметри студента
    name = request.form.get('name')
    age = request.form.get('age')
    ave = request.form.get('ave')
    faculty_id = request.form.get('faculties_id')
    #перевірили дані на наявність
    if name and age and ave and faculty_id:
        #викликали функцію додавання студента
        insert_student(name, int(age), float(ave), int(faculty_id))
    return redirect('/')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)