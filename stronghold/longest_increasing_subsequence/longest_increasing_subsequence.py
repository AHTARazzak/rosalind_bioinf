import sys

the_data = open(sys.argv[1], "r").readlines()

dec_initiate = the_data[0].split("\n")[0]
the_thing = the_data[1].split()

the_numbers = []
for i in the_thing:
	the_numbers.append(int(i))

sorted_the_numbers = sorted(the_numbers)
index_replace = []
for i in sorted_the_numbers:
	index_replace.append(the_numbers.index(i))

print(index_replace)

