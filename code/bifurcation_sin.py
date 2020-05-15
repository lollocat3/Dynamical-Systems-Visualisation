import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pandas as pd
import math
num_points = int(input('how many points? '))
bool_save = str(input('save as pdf? '))
P=np.linspace(0.6,1,num_points)
m=0.7
X = []
Y = []
for u in tqdm(P):
    X.append(u)
    m = np.random.random()
    for n in range(1001):
      m= u*np.sin(3.14159*m)
    for l in range(1051):
      m= u*np.sin(3.14159*m)
    Y.append(m)
data = pd.DataFrame(X,Y).to_csv('/Users/lorenzo/Desktop/Python/bifurcation1.csv')
plt.plot(X, Y, ls='', marker=',')
plt.savefig('/Users/lorenzo/Desktop/Python/sin_bifurcation.pdf', bbox_inches = 'tight',
pad_inches = 0, transparent = True)
plt.show()