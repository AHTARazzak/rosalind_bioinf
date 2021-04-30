'''
Title: Enumerating k-mers Lexicographically
Rosalind ID: LEXF
URL: http://rosalind.info/problems/lexf
Goal: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
'''

import sys

data_file = open(sys.argv[1]).readlines()
symbols = data_file[0].split('\n')[0]
symbols_val = symbols.split()
length = data_file[1].split('\n')[0]

combin_num = len(symbols_val)**int(length)
list_of_combos = []
the_crunch = ([1] * int(length))

for i in range(combin_num):
	for column in range(len(the_crunch)):
		if (the_crunch[column] > len(symbols_val)):
			the_crunch[column + 1] += 1
			the_crunch[column] = 1
	list_of_combos += the_crunch
	the_crunch[0] += 1

list_of_combos = [list_of_combos[i:i + int(length)] for i in range(0, len(list_of_combos), int(length))]

convert_combos = []

for entry in list_of_combos:
	this_combo = []
	for element in entry:
		this_combo.append(symbols_val[element - 1])
	convert_combos.append("".join(this_combo))

STRING_LIST = []
for element in convert_combos:
	STRING_LIST.append("".join(element))

STRING_LIST.sort()
print(STRING_LIST)

outfile = open("submit_this.txt", "w")

outfile.write("\n".join(STRING_LIST))
#Ali Razzak