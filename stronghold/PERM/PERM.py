'''
Title: Enumerating Gene Orders
Rosalind ID: PERM
URL: http://rosalind.info/problems/perm
Goal: The total number of permutations of length n, followed by a list of all such permutations (in any order).
'''

import sys

the_number =  open(sys.argv[1], "r").read()
string_initiate = []
string_initiate = "".join([str(x + 1) for x in range(int(the_number))])

ini_str = string_initiate
 
output_file = open("output_file.txt", "a")

# Printing initial string
print("Initial string", ini_str)
  
# Finding all permuatation
result = []
  
def permute(data, i, length): 
    if i == length: 
        result.append(''.join(data) )
    else: 
        for j in range(i, length): 
            # swap
            data[i], data[j] = data[j], data[i] 
            permute(data, i + 1, length) 
            data[i], data[j] = data[j], data[i]  
permute(list(ini_str), 0, len(ini_str))
  
# Printing
print(len(result))
for this_row in result:
	row_string = ""
	for element in this_row:
		row_string += (element + " ")
	output_file.write(row_string + "\n")
#Ali Razzak