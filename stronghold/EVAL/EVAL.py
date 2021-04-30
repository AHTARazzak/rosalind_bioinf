'''
Title: Introduction to Random Strings
Rosalind ID: PROB
URL: http://rosalind.info/problems/prob
Goal: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
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

#outfile = open("submit.txt", "w")
#outfile.write(" ".join(probability_list))
#Ali Razzak
