import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pandas as pd
import math
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

plt.rc('xtick', labelsize=20)

num_points = int(input('how many points? '))
bool_save = str(input('save as pdf? '))
P=np.linspace(3.543,3.569 ,num_points)
m=0.7
X = []
Y = []
for u in tqdm(P):
    X.append(u)
    m = np.random.random()
    for n in range(1001):
      m=u*m*(1-m)
    for l in range(1051):
      m=u*m*(1-m)
    Y.append(m)
#data = pd.DataFrame(X,Y).to_csv('/Users/lorenzo/Desktop/Python/bifurcation.csv')
fig, ax = plt.subplots()
ax.arrow(3.5451,0.472, 0.0189, 0, linewidth = 0.1, length_includes_head = True, head_length = 0.001, color = 'black', lw = 0.1)
ax.arrow(3.563,0.472, -0.0189, 0, linewidth = 0.1, length_includes_head = True, head_length =0.001,color = 'black', lw = 0.1)
ax.arrow(3.5645,0.472, 0.0043, 0, linewidth = 0.1, length_includes_head = True, head_length = 0.001, color = 'black', lw = 0.1)
ax.arrow(3.5683,0.472, -0.0043, 0, linewidth = 0.1, length_includes_head = True, head_length =0.001,color = 'black', lw = 0.1)
ax.axis([3.54, 3.569, 0.47, 0.56])
plt.ylabel(r'$x$', fontsize = 20)
plt.xlabel(r'$r$', fontsize = 20) 
ax.xaxis.set_label_coords(1.05, +0.02)
plt.xticks([3.554, 3.5665], (r'$\Delta_n$', r'$\Delta_{n+1}$'))
ax.plot(X, Y, ls='', marker=',')
plt.savefig('/Users/lorenzo/Desktop/Python/logistic_bifurcation3.pdf', bbox_inches = 'tight',
pad_inches = 0.1, transparent = True)
plt.show()
