'''
Title: Finding Disjoint Motifs in a Gene
Rosalind ID: ITWV
URL: http://rosalind.info/problems/itwv
Goal: An n×n matrix M for which Mj,k=1 if the jth and kth pattern strings can be interwoven into s and Mj,k=0 otherwise.
'''
from numpy import zeros
import sys

def check_interweave(dna1, dna2, superstr):
    if len(superstr) == 0:
        return True
    elif dna1[0] == dna2[0] == superstr[0]:
        return check_interweave(dna1[1:], dna2, superstr[1:]) or check_interweave(dna1, dna2[1:], superstr[1:])
    elif dna1[0] == superstr[0]:
        return check_interweave(dna1[1:], dna2, superstr[1:])
    elif dna2[0] == superstr[0]:
        return check_interweave(dna1, dna2[1:], superstr[1:])
    else:
        return False


with open(sys.argv[1]) as input_data:
	superstr = input_data.readline()
	dna = [line.strip() for line in input_data.readlines()]

M = zeros((len(dna), len(dna)), dtype=int)

for i in range(len(dna)):
	for j in range(len(dna)):
		if i <= j:
			current_profile = [(dna[i]+dna[j]).count(nucleotide) for nucleotide in 'ACGT']
                # Compare the current profile to each substring of the same length in the superstring.
			for index in range(len(superstr)-len(dna[i])-len(dna[j])+1):
                    # Having an identical profile is a necessary condition in order to be interweavable, but less computationally intensive.
				if current_profile == [superstr[index:index+len(dna[i])+len(dna[j])].count(nucleotide) for nucleotide in 'ACGT']:
                        # Check interweavability if the profiles match, add an extra character outside the alphabet to avoid index out of range errors.
					if check_interweave(dna[i]+'$', dna[j]+'$', superstr[index:index+len(dna[i])+len(dna[j])]):
						M[i][j] = 1
						break
		else:
			M[i][j] = M[j][i]

with open('submit.txt', 'w') as output_data:
	output_data.write('\n'.join([' '.join(map(str, M[i])) for i in range(len(dna))]))

#Ali Razzak