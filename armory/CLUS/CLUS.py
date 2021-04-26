'''
My solution to Rosalind Bioinformatics Problem CLUS
Title: Global Multiple Alignment
Rosalind ID: CLUS
http://rosalind.info/problems/clus/
Goal: ID of the string most different from the others.
'''
import os
import sys

os.system("clustalo --outfmt=fa --output-order=tree-order --force -i " + sys.argv[1] + " -o CLUS.output")

print(open("CLUS.output").readlines()[0][1:])

#Ali Razzak