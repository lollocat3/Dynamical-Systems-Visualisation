import matplotlib.pyplot as plt
import numpy as np
import math
from tqdm import tqdm
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

r = np.linspace(3, 4, 1000)

start = 0.3

def logistic(r, x):
  x = r*x*(1-x)
  return x


final = []

for lamda in tqdm(r):
  lyap = 0
  for i in range(300):
    x = logistic(lamda, start)
    start = x
  for i in range(10000):
    x = logistic(lamda, start)
    start = x
    lp = math.log(abs(lamda-2*lamda*x))
    lyap = lyap+lp
  lyap = lyap / 10000
  final.append(lyap)

plt.axis([3, 4, -1, 1])
plt.axhline(0, color='k')
plt.ylabel(r'$\lambda$', fontsize = 20)
plt.xlabel(r'$r$', fontsize = 20)
plt.plot(r, final,  '-o', markersize = 0.3)
plt.savefig('/Users/lorenzo/Desktop/Python/logistic_lyapanov.pdf', bbox_inches = 'tight',
    pad_inches = 0.1, transparent = True)
plt.show()

