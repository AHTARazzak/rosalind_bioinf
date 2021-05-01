'''
Title: Finding a Shared Spliced Motif
Rosalind ID: LCSQ
http://rosalind.info/problems/lcsq/
Goal: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
'''
import numpy as np
from Bio import SeqIO
import sys

def LCSQ(seq1, seq2):
	return backtrack(LCSQmatrix(seq1, seq2), seq1, seq2)

def LCSQmatrix(seq1, seq2):
	C = np.zeros((len(seq1) + 1, len(seq2) + 1), dtype=np.int)
	for i in range(1, len(seq1) + 1):
		for j in range(1, len(seq2) + 1):
			if seq1[i - 1] == seq2[j - 1]:
				C[i, j] = C[i - 1, j - 1] + 1
			else:
				C[i, j] = max(C[i, j - 1], C[i - 1, j])
	return C

def backtrack(C, seq1, seq2):
	lcsq = ''
	i, j = len(seq1), len(seq2)
	while i != 0 and j != 0:
		if seq1[i -  1] == seq2[j - 1]:
			lcsq = seq1[i -  1] + lcsq
			i -= 1
			j -= 1
		elif C[i, j] == C[i  - 1, j]:
			i -= 1
		else:
			j -= 1
	return lcsq

input_handle = sys.argv[1]
raw_data = list(SeqIO.parse(input_handle, 'fasta'))
sequences = list()
for seq in raw_data:
	sequences.append(str(seq.seq))

lcsq = LCSQ(sequences[0], sequences[1])
o = open("submit.txt", 'w')
o.write(lcsq)
o.close()

'''
from Bio import ExPASy
from Bio import SwissProt
from Bio import SeqIO
import sys
import os

def shared_find(main_seq, to_compare):
	shared_seq = str()
	for i in main_seq:
		if i in to_compare:
			#print(main_seq)
			#print(to_compare)
			this_index = to_compare.find(i)
			#print(this_index)
			shared_seq += i
			#print(shared_seq)
			to_compare = to_compare[this_index + 1:]
		#sto_compare = to_compare[1:]
	return(shared_seq)

the_sequences = list()

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		the_sequences.append(str(record.seq))

same_seq = list()

for i in range(len(the_sequences[0])):
	same_seq.append(shared_find(the_sequences[0][i:], the_sequences[1]))


for i in range(len(the_sequences[1])):
	same_seq.append(shared_find(the_sequences[1][i:], the_sequences[0]))

same_seq.sort(key=len)

print(same_seq[::-1][0])
'''
#Ali Razzak