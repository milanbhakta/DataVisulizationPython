import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import PIL
import requests

np.random.seed(950)
x = np.arange(50)
y = np.random.randint(0, 100, 50)
fig, ax = plt.subplots(figsize=(5, 3))

# scatter plot
# ax.scatter(x,y)

# bar plot
# ax.bar(x,y)
# ax.barh(x,y) #horizontal bar graph

# line plot
# ax.plot(x, y)

# histogram plot
# ax.hist(y)

# fonts
font1 = {'family': "sans-serif", 'color': 'blue', 'size': 20}
font2 = {'family': 'monospace', 'color': 'green', 'size': 14}

# Labels
ax.set_title('Total growth over time', fontdict=font1)
ax.set_ylabel('Total growth', fontdict=font2)
ax.set_xlabel('Years since start', fontdict=font2)
fig.tight_layout()


# customize plots

# scatter
# ax.scatter(x,y,marker='o',color="indigo")

# line plot
ax.plot(x,y,marker='o',color="indigo",linestyle="--",linewidth = 1)

ax.grid(axis='y',color="red",linewidth=2,linestyle='dotted')