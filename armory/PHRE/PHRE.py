'''
My solution to Rosalind Bioinformatics Problem PHRE
Title: Read Quality Distribution
Rosalind ID: PHRE
http://rosalind.info/problems/phre/
Goal: The number of reads whose average quality is below the threshold.
'''

from Bio import Entrez
from Bio import SeqIO
import statistics
import sys
import os

the_threshold = int(open(sys.argv[1], "r").readlines()[0].split("\n")[0])

fastq_open = open("cool.txt", "w")
fastq_open.write("".join(open(sys.argv[1], "r").readlines()[1:]))
fastq_open.close()

count = 0

with open("cool.txt") as fastq_file:
	for record in SeqIO.parse(fastq_file, "fastq"):
		if the_threshold > (statistics.mean(record.letter_annotations["phred_quality"])):
			count += 1

print(count)

#Ali Razzak
