'''
Title: Matching Random Motifs
Rosalind ID: RSTR
URL: http://rosalind.info/problems/rstr
Goal: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.
'''

import sys
import numpy as np

the_data = open(sys.argv[1]).readlines()

the_seq = the_data[1].split("\n")[0]
gc_prob = the_data[0].split("\n")[0].split()[1]
the_num = int(the_data[0].split("\n")[0].split()[0])

prob_gc = float(gc_prob) / 2
prob_at = (1 - float(gc_prob)) / 2
cumulative_stat = 1
for nt in the_seq:
	if nt == ("A") or nt == ("T"):
		cumulative_stat = cumulative_stat * prob_at
	if nt == ("G") or nt == ("C"):
		cumulative_stat = cumulative_stat * prob_gc

print(round(1-((1-cumulative_stat)**the_num),3))
#Ali Razzak