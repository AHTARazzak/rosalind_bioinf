'''
My solution to Rosalind Bioinformatics Problem SUBO
Title: Suboptimal Local Alignment
Rosalind ID: SUBO
http://rosalind.info/problems/subo/
Goal: The total number of occurrences of r as a substring of s, followed by the total number of occurrences of r as a substring of t.

'''
from Bio import SeqIO
from Bio.Seq import Seq
import sys
import os

def SuboptimalLocalAlignment(dna1, dna2, maxMismatches_d=3, minRepeatSize=32, maxRepeatSize=40):
    large = dna1 if len(dna1) > len(dna2) else dna2
    mk1, mk2 = 0, 0
    for i in range(len(large)-minRepeatSize+1):
        for j in range(maxRepeatSize-minRepeatSize+1):
            kmer = large[i:i+minRepeatSize+j]
            k1 = ApproximatePatternMatching(kmer, dna1, maxMismatches_d, True)
            k2 = ApproximatePatternMatching(kmer, dna2, maxMismatches_d, True)
            mk1, mk2 = max(mk1, len(k1)), max(mk2, len(k2))
    return (mk1, mk2)

def ApproximatePatternMatching(dnaPattern, dnaText, maxMismatches_d, resultAsArray=False):
    patternLength = len(dnaPattern)
    solutionIndexes = []
    for i in range(len(dnaText)-patternLength+1):
        dna1 = dnaText[i : i+patternLength]
        hammingDistance = HammingDistance(dna1, dnaPattern)
        if hammingDistance <= maxMismatches_d:
            solutionIndexes.append(i)
    if resultAsArray:
        return solutionIndexes
    else:
        return ' '.join([str(i) for i in solutionIndexes])

def HammingDistance(dna1, dna2):
    distance = sum(1 for i, j in zip(dna1, dna2) if i != j)
    return distance

the_sequences = []

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		the_sequences.append(str(record.seq))

print(SuboptimalLocalAlignment(the_sequences[0], the_sequences[1]))

'''
count = 0

with open(sys.argv[1]) as fasta_file:
	for record in SeqIO.parse(fasta_file, "fasta"):
		count += 1
		SeqIO.write(record, "file_" + str(count) + ".txt", 'fasta')

os.system("lalign36 file_1.txt file_2.txt > lalgin_file_1.txt")
os.system("lalign36 file_2.txt file_1.txt > lalgin_file_2.txt")

for element in range(1, count + 1):
	this_many = 0
	this_file = open("lalgin_file_" + str(element) + ".txt", "r").read().split("Waterman-Eggert")[1:]
	for entry in this_file:
		for line in entry.split("\n"):
			if " nt " in line:
				if (int(line.split()[5]) >=32) and (int(line.split()[5]) <= 40):
					if (entry.split("\n")[5].count(":")) >= (int(line.split()[5]) - 3):
						this_many += 1


	print(this_many)
'''
#Ali Razzak
