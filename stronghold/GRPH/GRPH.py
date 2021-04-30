'''
Title: Overlap Graphs
Rosalind ID: GRPH
URL: http://rosalind.info/problems/grph
Goal: The adjacency list corresponding to O3. You may return edges in any order.
'''

from Bio import SeqIO
from Bio.SeqUtils import GC

the_fasta_file = input("Name of file please: ")
fasta_file = open(the_fasta_file, 'r')

record_dictionary = {}

out_file = open("collected_items.txt", "a")

with open(the_fasta_file) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		record_dictionary[record.id] =  str(record.seq)

id_list = list(record_dictionary.keys())
seq_list = list(record_dictionary.values())

for rec_id, rec_seq in record_dictionary.items():
	for listed_seq in seq_list:
		if rec_seq != listed_seq:
			if rec_seq[-3:] == listed_seq[:3]:
				found_seq = seq_list.index(listed_seq)
				out_file.write(rec_id + " " + id_list[found_seq] + "\n")

#Ali Razzak