'''
My solution to Rosalind Bioinformatics Problem 021
Title: Locating Restriction Sites
Rosalind ID: REVP
Rosalind #: 021
URL: http://rosalind.info/problems/revp
Goal to return the position and length of every reverse palindrome in sequence
between lengths 4 and 12.
'''
from Bio import SeqIO
import sys

f = open(sys.argv[1], 'r')
seq = SeqIO.read(f, "fasta")
f.close()

outhandle = open("021_REVP.txt", 'w')
for start in range(len(seq)):
    for end in range(len(seq), start, -1): # iterate through all combinations of subsequences
        if end - start < 4: # try to save some time with lower length sequences
            break
        else:
            # check if reverse palindrome
            if str(seq.seq[start:end]) == str(seq.seq[start:end].reverse_complement()):
                # verify length of subsequence
                if len(seq.seq[start:end]) >= 4 and len(seq.seq[start:end]) <= 12:
                    # print to file, make sure strings for joining
                    print(" ".join(map(str, [start+1, len(seq.seq[start:end])])), file = outhandle)
outhandle.close()
