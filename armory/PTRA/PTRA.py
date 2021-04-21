'''
My solution to Rosalind Bioinformatics Problem PTRA
Title: Protein Translation
Rosalind ID: PTRA
http://rosalind.info/problems/ptra/
Goal: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)
'''
from Bio.Seq import translate
import sys

original_seq = open(sys.argv[1], "r").readlines()[0].split()[0]
compare_seq = translate(original_seq, stop_symbol="")
check_aa = open(sys.argv[1], "r").readlines()[1]

for element in range(len(compare_seq)):
	if compare_seq[element] != check_aa[element]:
		print(original_seq[(element * 3):((element * 3) + 3)] + " " + check_aa[element])

for i in range(1,7):
	compare_seq = translate(original_seq, table = i, stop_symbol="")
	if compare_seq.split()[0] == check_aa.split()[0]:
		print(i)

#Ali Razzak