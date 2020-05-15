from matplotlib import pyplot as plt 
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

def plot(a, x0=0.1, iterations=50):
	#if x0 <= 0 or x0 >= 1: return
	plt.title(r'$\textrm{Cobweb Plot:} \; f(x_n) = e^{-x_n}$', fontsize = 20)
	plt.xlabel(r'$x_n$', fontsize = 20)
	plt.ylabel(r'$x_{n+1}$', fontsize = 20)

	x = np.linspace(0, 3.5, 1000)
	fx = np.exp(-x)	
	plt.plot(x, fx, label=r"$f(x_n) = e^{-x_n}$")
	plt.legend(fontsize = 15)
	
	plt.plot([0, 1.2], [0, 1.2], color="red", label = r'$f(x_n) = x_n$')
	plt.legend(fontsize = 15)

	last_x, last_y = x0, 0
	for _ in range(iterations):
		#next_x = a * last_x * (1 - last_x)
		next_x = np.exp(- last_x)

		plt.plot([last_x, last_x], [last_y, next_x], color="black")
		
		plt.plot([last_x, next_x], [next_x, next_x], color="black")

		last_x, last_y = next_x, next_x
	plt.savefig('/Users/lorenzo/Desktop/Python/exp_cobweb.pdf', bbox_inches = 'tight',
    pad_inches = 0.1, transparent = True)
	plt.show()



def main():
	start = float(input('number : '))
	iterations = int(input('iterations: '))
	#parameter = float(input('parameter:'))
	plot(4, start, iterations)
	
	

if __name__ == "__main__":
	main()