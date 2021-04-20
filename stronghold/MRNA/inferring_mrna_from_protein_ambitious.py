import re
import sys

the_sequence =  open(sys.argv[1], "r")
the_seq = the_sequence.read().split()[0] + "-"

sequence_list = ["AUG"]

def add_codon(the_seq_list, new_seq_list, this_codon):
	for exis_seq in the_seq_list:
		for codon in this_codon:
			new_seq_list.append(exis_seq + codon)
		the_seq_list = new_seq_list
	return(the_seq_list)

def remove_stop(the_list):
	remove_list = []
	for check_sequence in range(len(the_list)):
		check_length = [m.start() for m in re.finditer(r"(?=(UAA|UGA|UAG))", the_list[check_sequence])]
		if len(check_length) > 0:
			remove_list.append(check_sequence)
	for index_rem in remove_list[::-1]:
		del the_list[index_rem]
	return(the_list)

for amino_acid in the_seq[1:]:
	print(amino_acid)
	new_sequence_list = []
	if amino_acid == "A":
		the_codon = ["GCU", "GCC", "GCA", "GCG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		sequence_list = remove_stop(sequence_list)
	if amino_acid == "R":
		the_codon = ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		sequence_list = remove_stop(sequence_list)
	if amino_acid == "N":
		the_codon = ["AAU", "AAC"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		sequence_list = remove_stop(sequence_list)
	if amino_acid == "D":
		the_codon = ["GAU", "GAC"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "C":
		the_codon = ["UGU", "UGC"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "Q":
		the_codon = ["CAA", "CAG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "E":
		the_codon = ["GAA", "GAG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "G":
		the_codon = ["GGU", "GGC", "GGA", "GGG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "H":
		the_codon = ["CAU", "CAC"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "I":
		the_codon = ["AUU", "AUC", "AUA"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "L":
		the_codon = ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "K":
		the_codon = ["AAA", "AAG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "M":
		the_codon = ["AUG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "F":
		the_codon = ["UUU", "UUC"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "P":
		the_codon = ["CCU", "CCC", "CCA", "CCG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "S":
		the_codon = ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "T":
		the_codon = ["ACU", "ACC", "ACA", "ACG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "W":
		the_codon = ["UGG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "Y":
		the_codon = ["UAU", "UAC"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "V":
		the_codon = ["GUU", "GUC", "GUA", "GUG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)
		remove_stop(sequence_list)
	if amino_acid == "-":
		the_codon = ["UAA", "UGA", "UAG"]
		sequence_list = add_codon(sequence_list, new_sequence_list, the_codon)

#print(sequence_list)
print(len(sequence_list))