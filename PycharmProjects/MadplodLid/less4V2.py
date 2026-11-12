import matplotlib.pyplot as plt

'''Стовбчата діаграма'''
a = [1000, 1500, 700, 500, 823]
b = ['Bob', 'Alice', 'Jone', 'Pit', 'Nike']

plt.bar(b, a, color=['r', 'g', 'y', 'b', 'yellow'], edgecolor='black', width=0.8)
plt.grid()
plt.xlabel("Name")
plt.ylabel("Vipay")
plt.title('NNN')
plt.show()
