'''
My solution to Rosalind Bioinformatics Problem DBPR
Title: Introduction to the Bioinformatics Armory
Rosalind ID: DBPR
http://rosalind.info/problems/dbpr/
Goal: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).
'''
from Bio.Seq import translate
import sys

original_seq = open(sys.argv[1], "r").readlines()[0].split()[0]
compare_seq = translate(original_seq, stop_symbol="")
check_aa = open(sys.argv[1], "r").readlines()[1]

#ensure_seq = "".join([element for element in compare_seq if element in aa_list])

for element in range(len(compare_seq)):
	if compare_seq[element] != check_aa[element]:
		print(original_seq[(element * 3):((element * 3) + 3)] + " " + check_aa[element])
#Ali Razzak
#
for i in range(1,7):
	compare_seq = translate(original_seq, table = i, stop_symbol="")
	if compare_seq.split()[0] == check_aa.split()[0]:
		print(i)