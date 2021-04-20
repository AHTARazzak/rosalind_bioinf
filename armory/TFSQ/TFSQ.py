'''
My solution to Rosalind Bioinformatics Problem TFSQ
Title: Introduction to the Bioinformatics Armory
Rosalind ID: TFSQ
http://rosalind.info/problems/tfsq/
Goal: Corresponding FASTA records
'''

from Bio import ExPASy
from Bio import SwissProt
from Bio import SeqIO
import sys
import os

with open(sys.argv[1], "rU") as input_handle:
    with open("the_submit.fasta", "w") as output_handle:
        sequences = SeqIO.parse(input_handle, "fastq")
        count = SeqIO.write(sequences, output_handle, "fasta")

print("Converted %i records" % count)

# os.system("sed -n '1~4s/^@/>/p;2~4p" + sys.argv[1] + " > out.fasta")


#Ali Razzak