'''
Title: Error Correction in Reads
Rosalind ID: CORR
URL: http://rosalind.info/problems/corr
Goal: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
'''

from Bio import SeqIO
import sys

def hamming_distance(s1, s2):
    return sum([1 if s1[i]!=s2[i] else 0 for i in range(len(s1))])

def error_correct(reads):
    corrections = list()
    correct_reads, incorrect_reads = list(), list()
    reverse_pattern={"A": "T", "T": "A", "C": "G", "G": "C"}

    for r in reads:
        reverse_r = "".join([reverse_pattern[i] for i in r[::-1]])
        if reads.count(r) + reads.count(reverse_r) >= 2:
            correct_reads.append(r)
        else:
            incorrect_reads.append(r)

    for ir in incorrect_reads:
        for cr in correct_reads:
            reverse_cr = "".join([reverse_pattern[i] for i in cr[::-1]])
            if hamming_distance(ir, cr) == 1:
                corrections.append((ir, cr))
                break
            if hamming_distance(ir, reverse_cr) == 1:
                corrections.append((ir, reverse_cr))
                break

    return corrections

seq_name, seq_string = [], []
with open (sys.argv[1],'r') as fasta_file:
	for seq_record in SeqIO.parse(fasta_file,'fasta'):
		seq_name.append(str(seq_record.name))
		seq_string.append(str(seq_record.seq))
corrections = error_correct(seq_string)
for ir, cr in corrections:
	print("{}->{}".format(ir, cr))

'''
seq_list = list()

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		seq_list.append(record.seq)

combo_list = list()

for i in range(len(seq_list)-1):
	for j in seq_list[:]:
		mismatch = 0
		mismatch_rp = 0
		for nt in range(len(str(seq_list[i]))):
			if str(seq_list[i])[nt] != str(j)[nt]:
				mismatch += 1
			if str(seq_list[i])[nt] != str(j.reverse_complement())[nt]:
				mismatch_rp += 1
		if (mismatch == 1):
			combo_list.append(str(seq_list[i])  + "->" + str(j))
		elif (mismatch_rp == 1):
			combo_list.append(str(seq_list[i])  + "->" + str(j.reverse_complement()))

no_dup_seq = list()
[no_dup_seq.append(x) for x in combo_list if x not in no_dup_seq]

print(no_dup_seq)
'''
#Ali Razzak