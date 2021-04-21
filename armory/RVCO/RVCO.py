'''
My solution to Rosalind Bioinformatics Problem RVCO
Title: Complementing a Strand of DNA
Rosalind ID: RVCO
http://rosalind.info/problems/rvco/
Goal: The number of given strings that match their reverse complements.
'''
from Bio import SeqIO
from Bio.Seq import Seq
import sys

reverse_number = 0

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		if str(record.seq) == (record.seq).reverse_complement():
			reverse_number += 1

print(reverse_number)

#Ali Razzak