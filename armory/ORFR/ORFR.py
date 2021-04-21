'''
My solution to Rosalind Bioinformatics Problem ORFR
Title: Finding Genes with ORFs
Rosalind ID: ORFR
http://rosalind.info/problems/orfr/
Goal: The longest protein string that can be translated from an ORF of s. If more than one protein string of maximum length exists, then you may output any solution.
'''

from Bio import Entrez
from Bio import SeqIO
import sys
import os

in_file = open(sys.argv[1], "r").readlines()[0].split("\n")[0]

os.system("getorf -sequence asis:" + in_file + " -outseq cool.txt -find 1")

trans_seq_list = []

with open("cool.txt") as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		trans_seq_list.append(str(record.seq))

print(sorted(trans_seq_list, key=len)[-1])



#Ali Razzak