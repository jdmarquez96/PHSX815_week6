import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import math 
from scipy import integrate
import sympy as sym
from Random import Random




def f(x): #gumbel density distribution
        return np.exp(-(x + np.exp(-x)))
xmin = -3
xmax = 3
random = Random()

def SampleFlat():
        return xmin + (xmax-xmin)*random.rand()


def montecarlo(n):
	sum = 0
	for i in range(0, n):
		X = SampleFlat()
		sum +=  (xmax - xmin)*f(X)
	average = sum/n
	return average



print("Montecarlo integration", montecarlo(10000))



#trapezoid integration method
def trap(f, b, a, n): #f is function, and n is the number of rectangles
        h = (b-a)/float(n)
        intgr = 0.5 * h*(f(a) + f(b))
        for i in range(1, int(n)):
                intgr += f(a + i*h)
        intgr *= h
        return intgr

print("trapezoidal integration", trap(f, 3, -3, 10000))
#true value with regular integration

x = sym.Symbol('x', real=True) #use to get the exact answer


ff = sym.exp(-(x + sym.exp(-x)))


answer = sym.integrate(ff, (x, -3,3))
print("True answer",answer)
Vanswer = np.exp(-np.exp(-3)) - np.exp(-np.exp(3))
print("True answer value", Vanswer)


def Error(n):
	error = (Vanswer - montecarlo(n))/Vanswer
	errortrap = (Vanswer - trap(f, 3, -3, n))/Vanswer
	return error ,errortrap


print("error with the true answer against montecarlo and trapezoid with 100 number of points", Error(100))
print("error with the true answer against montecarlo and trapezoid with 1000 number of points", Error(1000))
print("error with the true answer against montecarlo and trapezoid with 10000 number of points", Error(10000))
print("error with the true answer against montecarlo and trapezoid with 100000 number of points", Error(100000))
print("From what I see, the trapezoidal integration works better than the montecarlo integration for the 1-D gumbel distribution")
















