'''
Title: Introduction to Set Operations
Rosalind ID: SETO
URL: http://rosalind.info/problems/seto
Goal: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
'''
import sys

data = []
with open(sys.argv[1],'r') as f:
    for line in f:
        data.append(line.strip('\n'))

U = set(range(1, int(data[0])+1))
A = set([int(x) for x in data[1].strip('{}').split(',')])
B = set([int(x) for x in data[2].strip('{}').split(',')])

union = A.union(B)
intersection = set(A).intersection(B)
diff_AB = A-B
diff_BA = B-A
A_comp = U-A
B_comp = U-B

print(union)
print(intersection)
print(diff_AB)
print(diff_BA)
print(A_comp)
print(B_comp)

#Ali Razzak