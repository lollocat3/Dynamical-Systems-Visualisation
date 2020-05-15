import matplotlib.pyplot as plt
import numpy as np
import math
from tqdm import tqdm


r = np.linspace(0.001, 1, 1000)

start = 0.3

def logistic(r, x):
  x = r*x*(1-x)
  return x

def exponential(r, x):
  x = r*(-math.exp(2.987*x-1.841)+2.987*x+0.159)
  return x

final = []

for lamda in tqdm(r):
  lyap = 0
  for i in range(300):
    x =  exponential(lamda, start)
    start = x
  for i in range(10000):
    x = exponential(lamda, start)
    start = x
    #lp = math.log(abs(lamda-2*lamda*x))
    lp = math.log(abs(lamda*(2.987-2.987*math.exp(2.987*x-1.841))))
    lyap = lyap+lp
  lyap = lyap / 10000
  final.append(lyap)

plt.axis([0.6, 1, -1, 1])
plt.axhline(0, color='k')
plt.plot(r, final,  '-o', markersize = 0.3)
plt.savefig('/Users/lorenzo/Desktop/Python/exp_lyapanov.pdf', bbox_inches = 'tight',
    pad_inches = 0, transparent = True)
plt.show()

