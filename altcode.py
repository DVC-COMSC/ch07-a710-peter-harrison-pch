import numpy as np
import matplotlib.pyplot as plt

data1 = [100, 90, 80, 60]
data2 = [90, 80, 70, 100]
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

datab = []
for i in range(4):
    subjectrow = [labels[i], data1[i], data2[i]]
    datab.append(subjectrow)

x = np.arange(len(names))  # the label locations
width = 0.35 / 2  # the width of the bars

# using dist from edges and subject number index
def makebarm(num, subj): 
    return ax.bar(x - width*num, datab[subj][1:], width, label = datab[subj][0])

# copy of function for making bar right of center to go right, unsure of parsing so unfortunately make a new one with just - -> +
def makebarp(num, subj): 
    return ax.bar(x + width*num, datab[subj][1:], width, label = datab[subj][0])

#each subjects bars added
rects1 = makebarm(1.5, 0)
rects2 = makebarm(.5, 1)
rects3 = makebarp(.5, 2)
rects4 = makebarp(1.5, 3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title(f'Scores of {names[0]} and {names[1]}')
ax.set_xticks(x, names)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)

fig.tight_layout()

plt.show()

fig.savefig('altgraph.png')
