'''
Title: Inferring Protein from Spectrum
Rosalind ID: SPEC
URL: http://rosalind.info/problems/spec
Goal: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
'''
import sys

the_table = open("mass_table.txt", "r")

convert_table = {}

for line in the_table:
	this_line = line.split()
	if len(this_line) > 0:
		convert_table[round(float(this_line[1]),2)] = (this_line[0])

these_masses = open(sys.argv[1] , "r")

masses_list = []

the_aa = ""

for line in these_masses:
	masses_list.append(line)
	if len(masses_list) > 1:
		the_aa += convert_table[round((float(masses_list[-1]) - float(masses_list[0])), 2)]
		masses_list.pop(0)
				
print(the_aa)

#Ali Razzak