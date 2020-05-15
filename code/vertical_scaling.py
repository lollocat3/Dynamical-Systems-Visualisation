import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pandas as pd
import math
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
plt.rc('ytick', labelsize=20)

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
ax.arrow(3.554,0.5, 0, 0.045, linewidth = 0.001, length_includes_head = True, head_length = 0.005, color = 'black', width = 0.0002)
ax.arrow(3.567,0.5, 0, -0.0177, linewidth = 0.001, length_includes_head = True, head_length = 0.005, color = 'black', width = 0.0002)

ax.axis([3.54, 3.569, 0.47, 0.56])
plt.ylabel(r'$x$', fontsize = 20)
plt.xlabel(r'$r$', fontsize = 20) 
ax.xaxis.set_label_coords(1.05, +0.02)
plt.text(3.555, 0.535, r'$d_n$', fontsize = 20)
plt.text(3.563, 0.475, r'$d_{n+1}$', fontsize = 20)
plt.plot([3.4, 3.569], [0.5, 0.5], color = 'black')
plt.yticks(ticks = [0.5], labels = [r'$x_m$'])
ax.plot(X, Y, ls='', marker=',')
plt.savefig('/Users/lorenzo/Desktop/Python/logistic_bifurcation4.pdf', bbox_inches = 'tight',
pad_inches = 0.1, transparent = True)
plt.show()
