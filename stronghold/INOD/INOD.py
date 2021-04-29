'''
Title: Counting Phylogenetic Ancestors
Rosalind ID: INOD
URL: http://rosalind.info/problems/inod
Goal: The number of internal nodes of any unrooted binary tree having n leaves.
'''
import sys


print(int(open(sys.argv[1], "r").readlines()[0].strip())-2)

#Ali Razzak