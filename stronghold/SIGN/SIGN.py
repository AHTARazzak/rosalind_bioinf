'''
Enumerating Oriented Gene Orderings
Rosalind ID: SIGN
http://rosalind.info/problems/sign/
Goal: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
'''
import sys
import math

def add_gene(existing_gene, the_genes):
	this_collection = list()
	for i in existing_gene:
		indiv_genes = str(i).split()
		check_list = list()
		for l in indiv_genes:
			check_list.append(math.sqrt((int(l)**2)))
		for j in the_genes:
			if math.sqrt(int(j)**2) not in check_list:
				this_collection.append(str(i) + " " + str(j))
	return(this_collection)

num_enumerations = int(open(sys.argv[1]).readlines()[0].strip())

possible_nums = list()

for i in range(-1 * num_enumerations, num_enumerations + 1):
	if i != 0:
		possible_nums.append(i)


change_nums = possible_nums 

for i in range(num_enumerations - 1):
	change_nums = add_gene(change_nums, possible_nums)

final_output = str(len(change_nums)) + "\n"
for i in change_nums:
	final_output += i + "\n"

submit_file = open("submit.txt","w")
submit_file.write(final_output)

#Ali Razzak