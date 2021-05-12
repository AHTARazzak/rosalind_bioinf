'''
Title: Edit Distance
Rosalind ID: EDIT
URL: http://rosalind.info/problems/edit
Goal: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.
'''
from Bio import SeqIO
import sys

def EditDistance(s, t):
    n = len(s)
    m = len(t)
    if n * m == 0:
        return n + m

    D = [ [0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left = D[i - 1][j] + 1
            down = D[i][j - 1] + 1
            left_down = D[i - 1][j - 1] 
            if s[i - 1] != t[j - 1]:
                left_down += 1
            D[i][j] = min(left, down, left_down)
    
    return D[n][m]

seq_name, seq_string = [], []
with open(sys.argv[1], "r") as fa:
	for seq_record in SeqIO.parse(fa, "fasta"):
		seq_name.append(seq_record.name)
		seq_string.append(str(seq_record.seq))
s, t = seq_string
print(EditDistance(s, t))


'''
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import sys
import os

the_sequences = list()

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		the_sequences.append(str(record.seq))

the_sequences.sort(key=len)

small_seq = the_sequences[0]
long_seq = the_sequences[1]

#for a in pairwise2.align.globalxd(long_seq, small_seq, -100, -10, 0, 0):
#	print(format_alignment(*a))

print(long_seq)
print(small_seq)

#os.system("needle -asequence asis:"+long_seq+" -bsequence asis:"+small_seq+" -gapopen 0 -gapextend 0 -outfile very_cool.txt")
#os.system("clustalo -i "+sys.argv[1]+ " --percent-id")
#os.system("water -asequence asis:"+long_seq+" -bsequence asis:"+small_seq+" -squick_asequence Y -gapopen 10.0 -gapextend 0.5 -outfile very_cool.txt")
'''
#Ali Razzak