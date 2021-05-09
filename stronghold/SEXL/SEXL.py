'''
Title: Sex-Linked Inheritance
Rosalind ID: SEXL
URL: http://rosalind.info/problems/sexl
Goal: An array B of length n in which B[k] equals the probability that a randomly selected female will be a carrier for the k-th gene.
'''
import numpy as np
import sys

the_data = open(sys.argv[1], "r").readlines()[0].strip()

for i in the_data.split():
    print(round(2*float(i)*(1-float(i)),3), end=" ")

#Ali Razzak