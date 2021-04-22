'''
Title: Comparing Spectra with the Spectral Convolution
Rosalind ID: CONV
URL: http://rosalind.info/problems/conv
Goal: The largest multiplicity of S1⊖S2, as well as the absolute value of the number x maximizing (S1⊖S2)(x) (you may return any such value if multiple solutions exist).
'''
import sys
from collections import Counter

first_set = open(sys.argv[1] , "r").readlines()[0].split()
second_set = open(sys.argv[1] , "r").readlines()[1].split()

the_masses = []

for this_i in first_set:
	for this_j in second_set:
		print(round(float(this_i),2))
		the_masses.append(abs(round(float(this_i) - float(this_j), 5)))

the_counts = Counter(the_masses)
print(the_counts)

#Ali Razzak
