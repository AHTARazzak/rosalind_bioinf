'''
Title: Independent Segregation of Chromosomes
Rosalind ID: INDC
URL: http://rosalind.info/problems/indc
Goal: An array A of length 2n in which A[k] represents the common logarithm of the probability that two diploid siblings share at least k of their 2n chromosomes (we do not consider recombination for now).
'''
import sys
import numpy as np

n = (int(open(sys.argv[1], "r").readlines()[0].strip()))

prob = 0.5
pr = 0
A = []
for i in range(2*n, 0, -1):
	pr += np.math.factorial(2*n)/(np.math.factorial(i)*np.math.factorial(2*n-i)) * np.power(prob,i)*np.power(1-prob, 2*n-i)
	A.append(round(np.log10(pr), 3))

for j in A[::-1]:
	print(j, end=" ")
#Ali Razzak