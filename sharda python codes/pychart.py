import matplotlib.pyplot as plt

fruits = ['apple', 'mango', 'orange', 'guava']
values = [67, 34, 100, 29]

plt.pie(values, labels=fruits)
plt.axis('equal')
plt.show()
