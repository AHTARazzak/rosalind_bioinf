'''
k-Mer Composition
Rosalind ID: KMER
http://rosalind.info/problems/kmer/
Goal: The 4-mer composition of s.
'''
import sys
import re
from Bio import SeqIO

the_bases = ["A", "C", "G", "T"]

def add_gene(existing_gene, the_bases):
	new_list = list()
	for i in existing_gene:
		for j in the_bases:
			new_list.append(i + j)
	return(new_list)

new_combos = the_bases
for i in range(len(the_bases) - 1):
	new_combos = add_gene(new_combos, the_bases)

print(new_combos)

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		the_sequence = (str(record.seq))

num_list = list()

for i in new_combos:
	matches = (re.finditer(r'(?=(' + i + "))", the_sequence))
	num_list.append(str(len([m.span() for m in matches])))

submit_file = open("submit.txt","w")
submit_file.write(" ".join(num_list))

#Ali Razzak
