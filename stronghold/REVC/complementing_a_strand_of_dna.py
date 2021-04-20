nucleotide_allowed = ["A", "T", "G", "C"]

the_sequence_file = input("Name of file please: ")

sequence_file = open(the_sequence_file, 'r')

the_sequence = sequence_file.read()

complement_sequence = ""

for nucleotide in the_sequence:
	if nucleotide in nucleotide_allowed:
		if nucleotide == "A":
			complement_sequence += "T"
		elif nucleotide == "T":
			complement_sequence += "A"
		elif nucleotide == "G":
			complement_sequence += "C"
		elif nucleotide == "C":
			complement_sequence += "G"

print(complement_sequence[::-1])