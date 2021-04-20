'''
My solution to Rosalind Bioinformatics Problem FRMT
Title: Introduction to the Bioinformatics Armory
Rosalind ID: FRMT
http://rosalind.info/problems/frmt/
Goal: The shortest of the strings associated with the IDs in FASTA format.
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
	the_combos.append((each_record.id, len(each_record.seq)))

the_combos = sorted(the_combos, key=lambda x: x[1])

shortest_seq = Entrez.efetch(db="nucleotide", id=[the_combos[0][0]], rettype="fasta")
os.system("esearch -db nucleotide -query " + the_combos[0][0] + " | efetch -format fasta > " + the_combos[0][0])

#Ali Razzak