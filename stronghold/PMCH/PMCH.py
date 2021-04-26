'''
My solution to Rosalind Bioinformatics Problem CLUS
Title: Global Multiple Alignment
Rosalind ID: CLUS
http://rosalind.info/problems/clus/
Goal: ID of the string most different from the others.
'''
from collections import Counter
from math import factorial
from Bio import SeqIO
import sys

f = open(sys.argv[1], 'r')
raw_data = SeqIO.read(f, "fasta")
f.close()
seq = str(raw_data.seq)

counts = Counter(seq)

pn = factorial(counts["A"])*factorial(counts["C"])

print(pn)

#Ali Razzak
