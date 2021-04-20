'''
My solution to Rosalind Bioinformatics Problem GBK
Title: Introduction to the Bioinformatics Armory
Rosalind ID: GBK
http://rosalind.info/problems/gbk/
Goal: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.
'''

from Bio import Entrez
import datetime
import sys

the_file = open(sys.argv[1], "r").readlines()

term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (the_file[0].split("\n")[0], the_file[1].split("\n")[0], the_file[2].split("\n")[0])
print(term)


Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.esearch(db="nucleotide", term = term)
record = Entrez.read(handle)
print(record["Count"])
the_id_list = record["IdList"]

for i in the_id_list:
	handle = Entrez.efetch(db="nucleotide", id=i, rettype="gb", retmode="text")
	print(handle.readline().strip())

#Ali Razzak