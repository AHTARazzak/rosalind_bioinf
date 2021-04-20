the_compare_file = input("Name of file please: ")

compare_file = open(the_compare_file, 'r')

the_compare = compare_file.read().split()

mismatch = 0

seq_1 = list(enumerate(the_compare[0], 0))
seq_2 = list(enumerate(the_compare[1], 0))

for i in range(len(seq_1)):
	if seq_1[i] != seq_2[i]:
		mismatch += 1

print(mismatch)