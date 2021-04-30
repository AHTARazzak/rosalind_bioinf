'''
Title: Introduction to Alternative Splicing
Rosalind ID: ASPC
URL: http://rosalind.info/problems/aspc
Goal: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000. In shorthand, ∑nk=m(nk).
'''

import sys
import numpy as np
import math

the_data = open(sys.argv[1]).readlines()

n = int(the_data[0].split()[0].strip())
m = int(the_data[0].split()[1].strip())

total = 0
for k in range(m, n + 1):
	total += math.factorial(n)  // (math.factorial(k) * math.factorial((n - k)))

print(format(total%1000000))
#Ali Razzak