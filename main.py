import numpy as np
import matplotlib.pyplot as plt

data1 = [100, 90, 80, 60]
data2 = [90, 80, 70, 100]
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

fig, ax = plt.subplots()

# ******************************
# Make your code
# ******************************

datab = []
for i in range(4):
    subjectrow = [lablels[i], data1[i], data2[i]]
    datas.append(subjectrow)

'''
math = [data1[0], data2[0]]
english = [data1[1], data2[1]]
physics = [data1[2], data2[2]]
computer = [data1[3], data2[3]]
'''

x = np.arange(len(names))  # the label locations
width = 0.35  # the width of the bars

def makebarm(num, subjectnum):
    return ax.bar(x - width/(2*num), datab[subjectnum][1:], width, label = datab[subjectnum][0])

def makebarp(num, subjectnum):
    return ax.bar(x + width/(2*num), datab[subjectnum][1:], width, label = datab[subjectnum][0])


#fig, ax = plt.subplots()
rects1 = makebarm(1, 1)
rects2 = makebarm(2, 2)
rects3 = makebarp(2, 3)
rects4 = makebarp(1, 4)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title(f'Scores of {names.join(" and")}')
ax.set_xticks(x, names)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

fig.tight_layout()

plt.show()

fig.savefig('A10.png')
