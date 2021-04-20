'''
My solution to Rosalind Bioinformatics Problem DBPR
Title: Introduction to the Bioinformatics Armory
Rosalind ID: DBPR
http://rosalind.info/problems/dbpr/
Goal: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).
'''

from Bio import ExPASy
from Bio import SwissProt
import sys

handle = ExPASy.get_sprot_raw(open(sys.argv[1], "r").readlines()[0].split()[0]) #you can give several IDs separated by commas
record = SwissProt.read(handle)

print(record.keywords)


#Ali Razzak