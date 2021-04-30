'''
Title: Translating RNA into Protein
Rosalind ID: PROT
URL: http://rosalind.info/problems/prot
Goal: The protein string encoded by s.
'''

from Bio.Seq import Seq

the_rna_file = input("Name of file please: ")
rna_file = open(the_rna_file, 'r')
the_rna = rna_file.read()

rna = Seq(the_rna)
print(str(rna.translate(to_stop=True)))
#Ali Razzak