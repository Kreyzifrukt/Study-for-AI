import matplotlib.pyplot as plt

# Данные для диаграммы
labels = [
    'Baton', 'Bread', 'Mudrost', 'Graph'
]
sizes = [23.9, 22.8, 56.2, 1.6,]

# Создание фигуры
plt.figure(figsize=(10, 7))

# Построение круговой диаграммы
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%', # Формат отображения процентов
    startangle=0,      # Начальный угол
    counterclock=False # Отрисовка по часовой стрелке, как на фото
)

# Заголовок
plt.title('List of product')

# Отображение
plt.show()
