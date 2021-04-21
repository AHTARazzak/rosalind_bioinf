'''
My solution to Rosalind Bioinformatics Problem FILT
Title: Read Filtration by Quality
Rosalind ID: FILT
http://rosalind.info/problems/filt/
Goal: Number of reads in filtered FASTQ entries
'''
from Bio import Entrez
from Bio import SeqIO
import statistics
import sys
import os

the_data = open(sys.argv[1], "r").readlines()[0].split("\n")[0]

the_thresh = the_data.split()[0]
the_perc = the_data.split()[1]

fastq_open = open("cool.txt", "w")
fastq_open.write("".join(open(sys.argv[1], "r").readlines()[1:]))
fastq_open.close()

total_count = 0

with open("cool.txt") as fastq_file:
	for record in SeqIO.parse(fastq_file, "fastq"):
		make_count = 0
		for qual_score in record.letter_annotations["phred_quality"]:
			if qual_score >= int(the_thresh):
				make_count += 1
		if round((make_count/len(record.letter_annotations["phred_quality"]))*100, 0) < int(the_perc):
			total_count += 1
print(total_count)

#Ali Razzak

