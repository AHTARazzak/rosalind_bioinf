'''
Title: Speeding Up Motif Finding
Rosalind ID: KMP
URL: http://rosalind.info/problems/kmp
Goal: The failure array of s.
'''
from Bio import SeqIO
import sys

def KMP_failure_table(seq):
    failure_array = [0] * len(seq)
    k = 0
    for i in range(2, len(seq)):
        while k > 0 and seq[k] != seq[i - 1]:
            k = failure_array[k - 1]
        # if subsequence starting or continuing
        if seq[k] == seq[i - 1]:
            k += 1
            # -1 for 0-indexing
        failure_array[i - 1] = k
    return failure_array

input_file = open(sys.argv[1], 'r')
raw = SeqIO.read(input_file, "fasta")
input_file.close()
this_seq = str(raw.seq)

o = open("submit.txt", 'w')
new_list = [str(x) for x in KMP_failure_table(this_seq)]
o.write(" ".join(new_list))

#Ali Razzak