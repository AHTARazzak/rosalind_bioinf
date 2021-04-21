'''
My solution to Rosalind Bioinformatics Problem SUBO
Title: Suboptimal Local Alignment
Rosalind ID: SUBO
http://rosalind.info/problems/subo/
Goal: The total number of occurrences of r as a substring of s, followed by the total number of occurrences of r as a substring of t.

'''
from Bio import SeqIO
from Bio.Seq import Seq
import sys
import os

count = 0

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		count += 1
		SeqIO.write(record, "file_" + str(count) + ".txt", 'fasta')

os.system("lalign36 file_1.txt file_2.txt > lalgin_file_1.txt")
os.system("lalign36 file_2.txt file_1.txt > lalgin_file_2.txt")

for element in range(1, count + 1):
	this_many = 0
	this_file = open("lalgin_file_" + str(element) + ".txt", "r").read().split("Waterman-Eggert")[1:]
	for entry in this_file:
		for line in entry.split("\n"):
			if " nt " in line:
				if (int(line.split()[5]) >=32) and (int(line.split()[5]) <= 40):
					if (entry.split("\n")[5].count(":")) >= (int(line.split()[5]) - 3):
						this_many += 1


	print(this_many)

#Ali Razzak
