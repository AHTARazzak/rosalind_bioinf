'''
Base Quality Distribution
Rosalind ID: BPHR
http://rosalind.info/problems/bphr/
Goal: Number of positions where mean base quality falls below given threshold
'''
from Bio import SeqIO
import statistics
import sys

the_threshold = int(open(sys.argv[1], "r").readlines()[0].split("\n")[0])

fastq_open = open("cool.txt", "w")
fastq_open.write("".join(open(sys.argv[1], "r").readlines()[1:]))
fastq_open.close()

count = 0

with open("cool.txt") as fastq_file:
	number_of_records = 0
	for record in SeqIO.parse(fastq_file, "fastq"):
		record_length = len(str(record.seq))
		number_of_records += 1

all_positions = [0] * record_length

with open("cool.txt") as fastq_file:
	for record in SeqIO.parse(fastq_file, "fastq"):
		for qual in range(len(record.letter_annotations["phred_quality"])):
			all_positions[qual] += record.letter_annotations["phred_quality"][qual]

for i in all_positions:
	if (i/number_of_records) < the_threshold:
		count += 1
print(count)

#Ali Razzak