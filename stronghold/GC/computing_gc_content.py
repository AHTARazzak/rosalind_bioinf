from Bio import SeqIO
from Bio.SeqUtils import GC

the_fasta_file = input("Name of file please: ")

fasta_file = open(the_fasta_file, 'r')

highest_desc = ""
highest_GC = 0

with open(the_fasta_file) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		if GC(record.seq) > highest_GC:
			highest_desc = record.id
			highest_GC = GC(record.seq)


print(highest_desc)
print("%.5f" % highest_GC)