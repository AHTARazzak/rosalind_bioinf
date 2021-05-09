'''
Title: Independent Segregation of Chromosomes
Rosalind ID: AFRQ
URL: http://rosalind.info/problems/afrq
Goal: An array B having the same length as A in which B[k] represents the probability that a randomly selected individual carries at least one copy of the recessive allele for the k-th factor.
'''
import numpy as np
import sys

the_data = open(sys.argv[1], "r").readlines()[0].strip()

for i in the_data.split():
	y = np.sqrt(float(i))
	x = 1-y
	print(round((2*y*x)+(y*y),3), end=" ")

#Ali Razzak
