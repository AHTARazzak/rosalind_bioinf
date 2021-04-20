from Bio import SeqIO
from Bio.SeqUtils import GC

the_fasta_file = input("Name of file please: ")

out_file = open("collected_items.txt", "a")

def print_list(func_list):
	func_string = ""
	for entry in func_list:
		func_string += str(entry) + " "
	return (func_string)

with open(the_fasta_file) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		matrix_length = len(str(record.seq))

A_mat = [0] * matrix_length
T_mat = [0] * matrix_length
C_mat = [0] * matrix_length
G_mat = [0] * matrix_length

with open(the_fasta_file) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		for element in range(len(str(record.seq))):
			if str(record.seq)[element] == "A":
				A_mat[element] = A_mat[element] + 1
			if str(record.seq)[element] == "T":
				T_mat[element] = T_mat[element] + 1
			if str(record.seq)[element] == "C":
				C_mat[element] = C_mat[element] + 1
			if str(record.seq)[element] == "G":
				G_mat[element] = G_mat[element] + 1

#pos_freq = 
consensus_seq = ""

for position in range(matrix_length):
	pos_freq = [A_mat[position], T_mat[position], C_mat[position], G_mat[position]]
	the_largest_pos = pos_freq.index(max(pos_freq))
	if the_largest_pos == 0:
		consensus_seq += "A"
	if the_largest_pos == 1:
		consensus_seq += "T"
	if the_largest_pos == 2:
		consensus_seq += "C"
	if the_largest_pos == 3:
		consensus_seq += "G"


out_file.write(consensus_seq + "\n")
out_file.write("A: " + print_list(A_mat)[:-1] + "\n")
out_file.write("C: " + print_list(C_mat)[:-1] + "\n")
out_file.write("G: " + print_list(G_mat)[:-1] + "\n")
out_file.write("T: " + print_list(T_mat)[:-1])