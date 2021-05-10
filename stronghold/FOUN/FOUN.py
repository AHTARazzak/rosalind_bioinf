'''
Title: Catalan Numbers and RNA Secondary Structures
Rosalind ID: FOUN
URL: http://rosalind.info/problems/foun
Goal: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.
'''
from scipy.special import comb
import numpy as np
import sys

def WrightFisher_GeneticDrift(N, m, g):
    q = m/(2*N)
    p = 1 - q
    prob = [comb(2*N,i) * (q**(i)) * (p**(2*N-i)) for i in range(1, 2*N+1)]
    for gen in range(1, g):
        gen_prob = []
        for t in range(1, 2*N+1):
            prob_t = [comb(2*N,t) * ((i/(2*N))**(t)) * ((1-(i/(2*N)))**(2*N-t)) for i in range(1, 2*N+1)]
            gen_prob.append(sum([prob_t[j] * prob[j] for j in range(2*N)]))
        prob = gen_prob
    return np.log10(1-sum(prob))

def foun(N, m, A):
    k = len(A)
    B = np.zeros([m, k])
    for i in range(m):
        for j in range(k):
            B[i,j] = WrightFisher_GeneticDrift(N, A[j], i+1)
    return B

with open(sys.argv[1], "r") as f:
	N, m = map(int, f.readline().strip().split())
	A = [int(i) for i in f.readline().strip().split()]
B = foun(N, m, A)
for b in B:
	for bb in b:
		print(bb, end=" ")
	print()

#Ali Razzak