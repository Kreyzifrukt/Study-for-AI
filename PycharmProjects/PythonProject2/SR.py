import numpy as np
import matplotlib.pyplot as plt

# ---------------- 1. Гістограма віку пасажирів ----------------
ages = np.random.normal(29.7, 14.5, 891)

plt.hist(ages, bins=30, color='#4C72B0', edgecolor='white')
plt.title("Розподіл віку пасажирів Титаніка")
plt.xlabel("Вік")
plt.ylabel("Кількість")
plt.grid(alpha=0.3, linestyle='--')
plt.show()


# ---------------- 2. Дві гістограми (вижили / ні) ----------------
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

survived_ages = np.random.normal(28.3, 11.9, 342)
not_survived_ages = np.random.normal(30.6, 14.1, 549)

ax[0].hist(survived_ages, bins=20, color='#55A868', alpha=0.8, edgecolor='white')
ax[0].set_title("Вижили")
ax[0].set_xlabel("Вік")
ax[0].grid(alpha=0.3, linestyle='--')

ax[1].hist(not_survived_ages, bins=20, color='#C44E52', alpha=0.8, edgecolor='white')
ax[1].set_title("Загинули")
ax[1].set_xlabel("Вік")
ax[1].grid(alpha=0.3, linestyle='--')

plt.show()


# ---------------- 3. Stackplot ----------------
classes_data = np.array([
    [216, 184, 491],
    [200, 180, 480],
    [220, 190, 500]
])

x = [1, 2, 3]
plt.stackplot(
    x,
    classes_data[:, 0],
    classes_data[:, 1],
    classes_data[:, 2],
    labels=['1 клас', '2 клас', '3 клас'],
    colors=['#E1AF00', '#A0A0A0', '#8C564B']
)

plt.legend(loc='upper left')
plt.title("Розподіл пасажирів за класами")
plt.xticks([1, 2, 3], ['Перша', 'Друга', 'Третя'])
plt.grid(alpha=0.3, linestyle='--')
plt.show()


# ---------------- 4. Stem графік ----------------
groups = ['1 кл', '2 кл', '3 кл']
diffs = [136 - 80, 87 - 97, 119 - 372]

plt.stem(groups, diffs, linefmt='#4C72B0', markerfmt='o', basefmt='gray')
plt.title("Відхилення кількості виживших від середнього")
plt.axhline(0, color='black', linewidth=0.8)
plt.grid(alpha=0.3, linestyle='--')
plt.show()


# ---------------- 5. Кругова діаграма ----------------
sizes = [342, 549]
labels = ['Вижили', 'Загинули']
colors = ['#55A868', '#C44E52']

plt.pie(sizes, labels=labels, autopct='%.1f%%', colors=colors, shadow=True)
plt.title("Виживаність на Титаніку")
plt.show()