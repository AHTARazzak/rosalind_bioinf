'''
My solution to Rosalind Bioinformatics Problem NEED
Title: Pairwise Global Alignment
Rosalind ID: NEED
http://rosalind.info/problems/frmt/
Goal: The maximum global alignment score between the DNA strings associated with these IDs.
'''

from Bio import Entrez
from Bio import SeqIO
import sys
import os

in_file = open(sys.argv[1], "r").readlines()[0].split("\n")[0]

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=[in_file], rettype="fasta")
records = list (SeqIO.parse(handle, "fasta")) 

the_combos = []

for each_record in records:
	the_combos.append(str(each_record.seq))

os.system("Needle -asequence asis:" + the_combos[0] + " -bsequence asis:" + the_combos[1] + " -gapopen 10 -gapextend 1 -outfile here.txt -endweight -endopen 10 -endextend 1")

#the_combos = sorted(the_combos, key=lambda x: x[1])

#shortest_seq = Entrez.efetch(db="nucleotide", id=[the_combos[0][0]], rettype="fasta")
#os.system("esearch -db nucleotide -query " + the_combos[0][0] + " | efetch -format fasta > " + the_combos[0][0])

#Ali Razzak