'''
Title: Inferring mRNA from Protein
Rosalind ID: MRNA
URL: http://rosalind.info/problems/mrna
Goal: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
'''
# This script does not dynamically eliminate STOP codons, which my more ambitious one tries to do... at a huge computational cost :()

from functools import reduce
from operator import mul

freq = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2,
    'F': 2, 'G': 4, 'H': 2, 'I': 3,
    'K': 2, 'L': 6, 'M': 1, 'N': 2,
    'P': 4, 'Q': 2, 'R': 6, 'S': 6,
    'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'STOP': 3
}

def load_dna_file(fname):
    with open(fname) as inf:
        dna = inf.read()
    return "".join(dna.split())   # removes all whitespace

def num_rna_strings(dna, modulo=None):
    if modulo:
        reduce_fn = lambda a, b: (a * b) % modulo
    else:
        reduce_fn = mul
    freqs = (freq[base] for base in dna)
    return reduce(reduce_fn, freqs, freq["STOP"])

def main():
    dna = load_dna_file("rosalind_mrna.txt")
    num = num_rna_strings(dna, 1000000)
    print("Answer is {}".format(num))

if __name__ == "__main__":
    main()
#Ali Razzak