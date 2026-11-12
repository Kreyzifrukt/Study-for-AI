import numpy as np
import matplotlib.pyplot as plt

# ---------------- 1. Гістограма віку пасажирів ----------------
ages = np.random.normal(29.7, 14.5, 891)

plt.hist(ages, bins=30, color='skyblue', edgecolor='black')
plt.title("Розподіл віку пасажирів Титаніка")
plt.xlabel("Вік")
plt.ylabel("Кількість")
plt.grid()
plt.show()


# ---------------- 2. Дві гістограми (вижили / ні) ----------------
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

survived_ages = np.random.normal(28.3, 11.9, 342)
not_survived_ages = np.random.normal(30.6, 14.1, 549)

ax[0].hist(survived_ages, bins=20, color='green', alpha=0.7)
ax[0].set_title("Вижили")
ax[0].set_xlabel("Вік")

ax[1].hist(not_survived_ages, bins=20, color='red', alpha=0.7)
ax[1].set_title("Загинули")
ax[1].set_xlabel("Вік")

plt.show()


# ---------------- 3. Stackplot (пасажири за класами по роках/групах) ----------------
classes_data = np.array([
    [216, 184, 491], # Класи пасажирів
    [200, 180, 480],
    [220, 190, 500]
])

x = [1, 2, 3]
plt.stackplot(x, classes_data[:,0], classes_data[:,1], classes_data[:,2],
              labels=['1 клас', '2 клас', '3 клас'], colors=['gold', 'silver', 'brown'])

plt.legend(loc='upper left')
plt.title("Розподіл пасажирів за класами")
plt.xticks([1, 2, 3], ['Перша', 'Друга', 'Третя'])
plt.grid()
plt.show()

# ---------------- 4. Stem графік (різниця виживаності за класами) ----------------
groups = ['1 кл', '2 кл', '3 кл']
diffs = [136 - 80, 87 - 97, 119 - 372] # приклади відхилень

plt.stem(groups, diffs)
plt.title("Відхилення кількості виживших від середнього")
plt.axhline(0, color='black', linewidth=0.5)
plt.grid()
plt.show()


# ---------------- 5. Кругова діаграма ----------------
sizes = [342, 549]
labels = ['Вижили', 'Загинули']
colors = ['#66b3ff', '#ff9999']

plt.pie(a, labels=b,autopct='%.2f', shadow=False)
plt.title("Виживаність на Титаніку")
plt.show()