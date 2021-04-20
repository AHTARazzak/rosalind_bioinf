import sys
import numpy as np

the_data = open(sys.argv[1]).readlines()

the_seq = the_data[0].split("\n")[0]
the_prob = the_data[1].split("\n")[0].split()

probability_list = []

for gc_prob in the_prob:
	print(gc_prob)
	prob_gc = float(gc_prob) / 2
	prob_at = (1 - float(gc_prob)) / 2
	cumulative_stat = 1
	for nt in the_seq:
		if nt == ("A") or nt == ("T"):
			cumulative_stat = cumulative_stat * prob_at
		if nt == ("G") or nt == ("C"):
			cumulative_stat = cumulative_stat * prob_gc
	probability_list.append(str(round(np.log10(cumulative_stat), 3)))

print(" ".join(probability_list))

outfile = open("submit.txt", "w")
outfile.write(" ".join(probability_list))