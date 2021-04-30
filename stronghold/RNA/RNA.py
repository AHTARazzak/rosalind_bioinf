'''
Title: Transcribing DNA into RNA
Rosalind ID: RNA
URL: http://rosalind.info/problems/rna
Goal: The transcribed RNA string of t.
'''

nucleotide_allowed = ["A", "U", "G", "C"]

the_sequence_file = input("Name of file please: ")

sequence_file = open(the_sequence_file, 'r')

the_sequence = sequence_file.read()

converted_sequence = the_sequence.replace("T", "U")
print(converted_sequence)
#Ali Razzak