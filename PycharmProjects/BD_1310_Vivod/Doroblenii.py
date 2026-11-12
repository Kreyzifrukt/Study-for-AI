import sqlite3


def create():
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Groups(
            group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL)""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Disciplines(
            discipline_id INTEGER PRIMARY KEY AUTOINCREMENT,
            discipline_name TEXT NOT NULL
        )""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students(
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            group_id INTEGER,
            FOREIGN KEY (group_id) REFERENCES Groups(group_id)
        )""")
    connect.commit()
    connect.close()


def add_group(g_name):
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Groups (group_name) VALUES (?)", (g_name,))
    connect.commit()
    connect.close()


def add_discipline(discipline_name):
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Disciplines (discipline_name) VALUES (?)", (discipline_name,))
    connect.commit()
    connect.close()


def add_student(full_name, g_id):
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Students(full_name, group_id) VALUES (?,?)", (full_name, g_id))
    connect.commit()
    connect.close()


def get_groups():
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Groups")
    data = cursor.fetchall()
    connect.close()
    return data


def get_discipline():
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Disciplines")
    data = cursor.fetchall()
    connect.close()
    return data


def get_students():
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    cursor.execute("""
        SELECT Students.student_id, Students.full_name, 
        Groups.group_name FROM Students LEFT JOIN Groups ON
        Students.group_id = Groups.group_id
    """)
    data = cursor.fetchall()
    connect.close()
    return data


def show_groups():
    groups = get_groups()
    print("\nГрупи")
    if groups:
        for group in groups:
            print(f"ID: {group[0]}, Назва групи: {group[1]}")
    else:
        print("Групи не знайдені")


def show_disciplines():
    disciplines = get_discipline()
    print("\n Дисципліни")
    if disciplines:
        for discipline in disciplines:
            print(f"ID: {discipline[0]}, Дисципліни: {discipline[1]}")
    else:
        print("Дисципліни не знайдені")


def show_students():
    students = get_students()
    print("\nСтуденти")
    if students:
        for student in students:
            student_id, full_name, group_name = student
            print(f"Ім'я: {full_name}, Група: {group_name} (ID: {student_id})")
    else:
        print("Студенти не знайдені")


if __name__ == "__main__":
    create()
    job = True
    while job:
        choice = int(input('1-AddGroup\n2-AddDiscipline\n3-AddStudent\n4-ShowGroups\n5-ShowDisciplines\n6-ShowStudents\n0-Exit\n'))

        if choice == 0:
            job = False
        elif choice < 1 or choice > 6:
            print("Wrong choice")
        elif choice == 1:
            group_name = input("Enter group name\n")
            if group_name.strip() == 0:
                print("Wrong name")
            else:
                add_group(group_name)
        elif choice == 2:
            discipline = input("Enter discipline\n")
            if discipline.strip() == 0:
                print("Wrong discipline")
            else:
                add_discipline(discipline)
        elif choice == 3:
            name = input("Enter name\n")
            if name.strip() == 0:
                print("Wrong name")
            else:
                try:
                    g_id = int(input("Enter group\n"))
                    add_student(name, g_id)
                except ValueError:
                    print("Wrong ID")
        elif choice == 4:
            show_groups()
        elif choice == 5:
            show_disciplines()
        elif choice == 6:
            show_students()
