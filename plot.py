
import numpy as np
import matplotlib.pyplot as plt
from math import log10


#bar chart https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
labels = ['5000', '500000', '5000000', '50000000']
python_running_time = []
debug_running_time = []
release_running_time = []

with open(r'C:\Users\30662\Desktop\time.csv','r') as f:
    lines=f.readlines()

for i in range(4):
    python_running_time.append(log10(float(lines[i * 3 + 1].split(',')[2])))
    debug_running_time.append(log10(float(lines[i * 3 + 2].split(',')[2])))
    release_running_time.append(log10(float(lines[i * 3 + 3].split(',')[2])))

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, python_running_time, width, label='Python')
rects2 = ax.bar(x, debug_running_time, width, label='C++debug')
rects3 = ax.bar(x + width, release_running_time, width, label='C++release')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Stimulation time',fontweight=800)
ax.set_ylabel('Running time (unit: log10(ms))',fontweight=800)
ax.set_title('Running time comparison',fontsize=20,fontweight=800)
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, fmt='%.2f',padding=3,fontsize=7.5)
ax.bar_label(rects2, fmt='%.2f',padding=3,fontsize=7.5)
ax.bar_label(rects3, fmt='%.2f',padding=3,fontsize=7.5)

fig.tight_layout()

plt.savefig(r'C:\Users\30662\Desktop\plot.png',dpi=300)