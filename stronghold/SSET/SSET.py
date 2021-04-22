'''
Title: Counting Subsets
Rosalind ID: SSET
URL: http://rosalind.info/problems/sset
Goal: The total number of subsets of {1,2,…,n} modulo 1,000,000.
'''
import sys

the_data = open(sys.argv[1], "r").readlines()[0].split()[0]

the_list = []

the_number = 1

for i in range(int(the_data)):
	the_number = the_number * 2

print(the_number % 1000000)

#Ali Razzak