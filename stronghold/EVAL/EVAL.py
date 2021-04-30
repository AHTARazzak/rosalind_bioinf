'''
Title: Expected Number of Restriction Sites
Rosalind ID: EVAL
URL: http://rosalind.info/problems/eval
Goal:  An array B having the same length as A in which B[i] represents the expected number of times that s will appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i] (see “Introduction to Random Strings”).
'''

import sys
import numpy as np

the_data = open(sys.argv[1]).readlines()

the_length = the_data[0].split("\n")[0]
the_subseq = the_data[1].split("\n")[0]
the_prob = the_data[2].split("\n")[0].split()

probability_list = []

multiple = int(the_length) - (len(the_subseq) - 1)

print(multiple)
for gc_prob in the_prob:
	print(gc_prob)
	prob_gc = float(gc_prob) / 2
	prob_at = (1 - float(gc_prob)) / 2
	cumulative_stat = 1
	for nt in the_subseq:
		if nt == ("A") or nt == ("T"):
			cumulative_stat = cumulative_stat * prob_at
		if nt == ("G") or nt == ("C"):
			cumulative_stat = cumulative_stat * prob_gc
	probability_list.append(str(round((cumulative_stat * multiple), 4)))

print(" ".join(probability_list))

outfile = open("submit.txt", "w")
outfile.write(" ".join(probability_list))
#Ali Razzak
