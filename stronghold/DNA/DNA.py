'''
Title: Counting DNA Nucleotides
Rosalind ID: DNA
URL: http://rosalind.info/problems/DNA
Goal: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

nucleotide_allowed = ["A", "T", "G", "C"]

the_sequence_file = input("Name of file please: ")

sequence_file = open(the_sequence_file, 'r')

the_sequence = sequence_file.read()

A_count = 0
T_count = 0
G_count = 0
C_count = 0

for nucleotide in the_sequence:
	if nucleotide in nucleotide_allowed:
		if nucleotide == "A":
			A_count += 1
		elif nucleotide == "T":
			T_count += 1
		elif nucleotide == "G":
			G_count += 1
		elif nucleotide == "C":
			C_count += 1

print(str(A_count) + " " + str(C_count) + " " + str(G_count) + " " + str(T_count))

#Ali Razzak