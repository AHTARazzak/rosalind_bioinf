from Bio import SeqIO, Seq
import re
import sys

sequence_list = []

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		sequence_list.append(str(record.seq))

sequence_one = sequence_list[0].split()[0]
sequence_two = sequence_list[1].split()[0]

print(sequence_two)

transversion = ["AC", "CA", "AT", "TA", "GC", "CG", "GT", "TG"]
transver_score = 0
transition = ["AG", "GA", "TC", "CT"]
transit_score = 0

for i in range(len(sequence_one)):
	the_couple = sequence_one[i] + sequence_two[i]
	print(the_couple)
	if the_couple in transversion:
		print("a")
		transver_score += 1
	if the_couple in transition:
		print("b")
		transit_score += +1

print(round(transit_score/transver_score,11))
