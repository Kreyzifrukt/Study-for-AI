class Chat:
    def __init__(self):
        self.messages = []

    def add_message(self, author, text):
        self.messages.append({"author": author, "text": text})
        print(f"Повідомлення від {author} додано.")

    def show_messages(self):
        print("Всі повідомлення:")
        for msg in self.messages:
            print(f"{msg['author']}: {msg['text']}")

    def search_by_author(self, author):
        print(f"Повідомлення від {author}:")
        for msg in self.messages:
            if msg["author"] == author:
                print(f"- {msg['text']}")

chat1 = Chat()
chat1.add_message("Іван", "Добрій дінь")
chat1.add_message("Галя Квіти", "Дібрій, шо знову квіти купити треба ?")
chat1.add_message("Іван", "тАК, Він ті, квіті бідь ласка")
chat1.show_messages()
chat1.search_by_author("Аня")
