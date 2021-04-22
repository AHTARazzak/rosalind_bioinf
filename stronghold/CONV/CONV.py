'''
Title: Comparing Spectra with the Spectral Convolution
Rosalind ID: CONV
URL: http://rosalind.info/problems/conv
Goal: The largest multiplicity of S1⊖S2, as well as the absolute value of the number x maximizing (S1⊖S2)(x) (you may return any such value if multiple solutions exist).
'''
import sys

the_table = open("mass_table.txt", "r")

convert_table = []

for line in the_table:
	this_line = line.split()
	if len(this_line) > 0:
		convert_table.append(round(float(this_line[1]),2))

these_masses = open(sys.argv[1] , "r").readlines()[0].split()

masses_list = []
count_this_list = []

for entry in these_masses:
	masses_list.append(entry)
	if len(masses_list) > 1:
		count_this_list.append(round((float(masses_list[-1]) - float(masses_list[-2])), 2))
		masses_list.pop(0)
				
print(count_this_list)

#Ali Razzak
