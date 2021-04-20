'''
My solution to Rosalind Bioinformatics Problem INI
Title: Introduction to the Bioinformatics Armory
Rosalind ID: INI
http://rosalind.info/problems/ini/
Goal: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must provide your answer in the format shown in the sample output below.
'''

import sys
from Bio.Seq import Seq

data_file = open(sys.argv[1], 'r').readlines()
the_sequence = data_file[0].split()[0]

print(str(the_sequence.count("A")) + " " + str(the_sequence.count("C")) + " " + str(the_sequence.count("G")) + " " + str(the_sequence.count("T")))

#Ali Razzak