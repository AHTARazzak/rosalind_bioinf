'''
Title: Creating a Distance Matrix
Rosalind ID: PDST
URL: http://rosalind.info/problems/pdst
Goal: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
'''
from Bio import SeqIO, Seq
import re
import sys

the_sequences = []

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		the_sequences.append(str(record.seq))

the_matrix = []

for this_sequence in the_sequences:
	this_line = []
	for compare_sequence in the_sequences:
		mismatch_count = 0
		for aa_i in range(len(this_sequence)):
			if this_sequence[aa_i] != compare_sequence[aa_i]:
				mismatch_count += 1
		#this_line.append(
		if len(str(round((mismatch_count / len(this_sequence)), 5))) < 8:
			this_line.append(str(round((mismatch_count / len(this_sequence)), 5)) + ("0" * (7 - len(str(round((mismatch_count / len(this_sequence)), 5))))))
		else:
			this_line.append(str(round((mismatch_count / len(this_sequence)), 5)))
	the_matrix.append(" ".join(this_line))

out_file = open("submit_file.txt", "w")
out_file.write("\n".join(the_matrix))
#Ali Razzak