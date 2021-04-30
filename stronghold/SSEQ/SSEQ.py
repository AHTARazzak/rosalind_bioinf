'''
Title: Finding a Spliced Motif
Rosalind ID: SSEQ
URL: http://rosalind.info/problems/sseq
Goal: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
'''

from Bio import SeqIO, Seq
import re
import sys

sequence_list = []

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		sequence_list.append(str(record.seq))

big_sequence = sequence_list[0].split()[0]
subseq = sequence_list[1].split()[0]

find_list = []

make_up = 0

for nt in subseq:
	this_spot = big_sequence.find(nt)
	find_list.append(str(make_up + this_spot + 1))
	make_up += this_spot + 2
	big_sequence = big_sequence[this_spot + 2:]

print(" ".join(find_list))
#Ali Razzak