'''
Title: Partial Permutations
Rosalind ID: PPER
URL: http://rosalind.info/problems/pper
Goal: The total number of partial permutations P(n,k), modulo 1,000,000.
'''

from math import factorial
import sys

the_data = open(sys.argv[1], 'r')
max_num, max_digits = map(int, the_data.readline().split())

solution = (factorial(max_num) / factorial(max_num - max_digits)) % 1000000
print(solution)
#Ali Razzak