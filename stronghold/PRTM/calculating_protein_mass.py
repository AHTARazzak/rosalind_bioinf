import sys

conv_mass_table = {}

with open("mass_table.txt") as mass_table:
	for amino_acid in mass_table:
		conv_mass_table[amino_acid.split()[0]] = amino_acid.split()[1]

total_mass = 0

with open(sys.argv[1]) as this_sequence:
	for the_seq in this_sequence:
		for aa in the_seq.split()[0]:
			total_mass += float(conv_mass_table[aa])


print(round(total_mass,3))