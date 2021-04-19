from Bio import SeqIO, Seq
import re
import sys

all_sequence = []

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		all_sequence.append(str(record.seq))

all_sequence.sort(key=len)
all_sequence.reverse()

main_seq = all_sequence[0]
print(main_seq)

for entry in all_sequence[1:]:
	print(entry)
	for match in re.finditer(entry, main_seq):
		main_seq = main_seq[:match.span()[0]] +  ((match.span()[1] - match.span()[0]) * "-") + main_seq[(match.span()[1]):]
		print(main_seq)

main_seq = main_seq.replace("-","")

print(len(main_seq))
print(main_seq)