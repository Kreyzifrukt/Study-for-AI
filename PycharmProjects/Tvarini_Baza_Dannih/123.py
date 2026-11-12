import json

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title, author, year):
        self.__books.append({"title": title, "author": author, "year": year})
        print(f"Книга '{title}' додана")

    def remove_book(self, title):
        for book in self.__books:
            if book["title"] == title:
                self.__books.remove(book)
                print(f"Книга '{title}' Видалена")
                return
        print(f"Книга '{title}' Не знайдена")

    def find_books_by_author(self, author):
        return [book for book in self.__books if book["author"] == author]

    def get_all_books(self):
        return self.__books

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.__books, f, ensure_ascii=False, indent=4)
            print(f"Бібліотека збережена у файлі {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.__books = json.load(f)
                print(f"Бібліотека завантажена с файлу {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено")

library = Library()
library.add_book("ОНО", "Стівен Кінг", 2000)
library.add_book("Абетка", "Авраменко", 2010)
library.add_book("Війна та Мир", "Лев Толстой", 2005)

print("Усі книги: ", library.get_all_books())
print("Книга Авраменко: ", library.find_books_by_author("Авраменко"))

library.remove_book("Війна та Мир")
library.save_to_file("library.json")

new_library = Library()
new_library.load_from_file("library.json")
print("Завантажені книги: ", new_library.get_all_books())
