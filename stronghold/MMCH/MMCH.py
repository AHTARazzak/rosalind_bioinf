'''
Title: Maximum Matchings and RNA Secondary Structures
Rosalind ID: MMCH
URL: http://rosalind.info/problems/mmch
Goal: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
'''
from math import factorial
import sys

the_seq = "".join(open(sys.argv[1], 'r').readlines()[1:]).replace("\n","")
#final_seq = "".join(the_seq)

A, U, G, C = 0, 0, 0, 0
for nt in the_seq:
    if nt == 'A':
        A += 1
    elif nt == 'U':
        U += 1
    elif nt == 'G':
        G += 1
    elif nt == 'C':
        C += 1

AU = factorial(max(A, U)) / factorial(max(A, U) - min(A, U))
GC = factorial(max(G, C)) / factorial(max(G, C) - min(G, C))
print(int(AU * GC))
#Ali Razzak