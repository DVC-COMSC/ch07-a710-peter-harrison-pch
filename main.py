import matplotlib.pyplot as plt

data1 = [100, 90, 80, 60]
data2 = [90, 80, 70, 100]
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

fig, ax = plt.subplots()

# ******************************
# Make your code
# ******************************

width = 0.7       # the width of the bars: can also be len(x) sequence

ax.bar(labels, data1, width, label= names[0])
ax.bar(labels, data2, width, bottom=data1, label = names[1])

ax.set_title(f'Scores by {names[0]} and {names[1]}')
ax.legend()

#plt.show()

fig.savefig('A10.png')
