'''
Title: The Wright-Fisher Model of Genetic Drift
Rosalind ID: WFMD
URL: http://rosalind.info/problems/wfmd
Goal: The probability that in a population of N diploid individuals initially possessing m copies of a dominant allele, we will observe after g generations at least k copies of a recessive allele. Assume the Wright-Fisher model.
'''
from scipy.special import comb
import sys

def WrightFisher_GeneticDrift(N, m, g, k):
    p = m/(2*N)
    q = 1 - p
    prob = [comb(2*N,i) * (q**(i)) * (p**(2*N-i)) for i in range(1, 2*N+1)]
    for gen in range(1, g):
        gen_prob = []
        for t in range(1, 2*N+1):
            prob_t = [comb(2*N,t) * ((i/(2*N))**(t)) * ((1-(i/(2*N)))**(2*N-t)) for i in range(1, 2*N+1)]
            gen_prob.append(sum([prob_t[j] * prob[j] for j in range(2*N)]))
        prob = gen_prob
    print("answer: ", round(sum(prob[k-1:]),3))
    return prob

with open(sys.argv[1], "r") as f:
    N, m, g, k = map(int, f.readline().strip().split())

WrightFisher_GeneticDrift(N, m, g, k)

#Ali Razzak