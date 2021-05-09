'''
Title: Genome Assembly as Shortest Superstring
Rosalind ID: LONG
URL: http://rosalind.info/problems/long
Goal: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
'''
from Bio import SeqIO
import sys

def _get_overlap_strings(s1, s2):
	combine_strings =  list()
	overlap_strings = list()
	for i in range(len(s1)):
		if s1[i:] == s2[:len(s1) - i]:
			overlap_strings.append(s1[i:])
			combine_strings.append(s1 + s2[len(s1) - i:])
			break
	for i in range(len(s2)):
		if s2[i:] == s1[:len(s2) - i]:
			overlap_strings.append(s2[i:])
			combine_strings.append(s2 + s1[len(s2) - i:])
			break
	if not overlap_strings:
		return "", ""

	combine_string = min(combine_strings, key=len)
	overlap_string = max(overlap_strings, key=len)
	return combine_string, overlap_string

def find_superstring(strings):
	temp = strings

	while len(temp) > 1:
		most_overlapping_string = ""
		most_overlapping_string_pair = []
		most_overlapping_string_length = 0
		for i in range(len(temp) - 1):
			for j in range(i + 1, len(temp)):
				combine_string, overlap_string = _get_overlap_strings(temp[i], temp[j])
				if len(overlap_string) > most_overlapping_string_length:
					most_overlapping_string = combine_string
					most_overlapping_string_pair = [temp[i], temp[j]]
					most_overlapping_string_length = len(overlap_string)

		temp.remove(most_overlapping_string_pair[0])
		temp.remove(most_overlapping_string_pair[1])
		temp.append(most_overlapping_string)
        
	return temp 

seq_name, seq_string = list(), list()
with open (sys.argv[1],'r') as fa:
	for seq_record  in SeqIO.parse(fa,'fasta'):
		seq_name.append(str(seq_record.name))
		seq_string.append(str(seq_record.seq))
shortest_superstring = find_superstring(seq_string)
print(shortest_superstring[0])

'''
from Bio import SeqIO
import sys
import os

sequence_list = list()
with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		sequence_list.append(str(record.seq))

compare_list = sequence_list[1:]
next_string = sequence_list[0]


for j in range(len(compare_list)):
	check_list = list()
	this_string = str()
	os.system("needle -asequence asis:" + next_string + " -bsequence asis:" + compare_list[j] + " -gapopen 100 -gapextend 10 -awidth3 1000 -outfile cool.txt")
	with open("cool.txt", 'r') as this_alignment:
		for line in this_alignment:
			split_line = line.split()
			if len(split_line) > 0:
				if split_line[0] == "asis":
					this_string += split_line[2].strip() + "|"
		check_list.append(this_string[:-2])
	length_list = [len(x) for x in check_list]
	print(check_list)
	print(length_list)
	index_of_shortest = length_list.index(min(length_list))
	shortest_seq = check_list[index_of_shortest]
	split_shorts = shortest_seq.split("|")
	if shortest_seq[0] == "-":
		find_start = split_shorts[0].rfind("-")
		next_string = split_shorts[1][:find_start] + next_string
	else:
		find_start = split_shorts[1].rfind("-")
		next_string = next_string[:find_start] + split_shorts[1][find_start:]
	#compare_list.pop(index_of_shortest)
'''
#Ali Razzak
