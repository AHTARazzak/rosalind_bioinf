'''
Title: Ordering Strings of Varying Length Lexicographically
Rosalind ID: LEXV
URL: http://rosalind.info/problems/lexv
Goal: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
'''

from itertools import product
import sys

the_data = open(sys.argv[1], 'r')
symbols = ''.join(the_data.readline().rstrip().split())
length = int(the_data.readline().rstrip())

perms = []
for perm in product(symbols, repeat=length):
    for element in range(1, length + 1):
        if perm[:element] not in perms:
            perms.append(perm[:element])

output_file = open("submit.txt", 'w')
for entry in perms:
    print >> output_file, ''.join(entry)
#Ali Razzak