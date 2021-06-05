'''
Title: Matching a Spectrum to a Protein
Rosalind ID: PRSM
URL: http://rosalind.info/problems/prsm
Goal: The maximum multiplicity of R⊖S[sk] taken over all strings sk, followed by the string sk for which this maximum multiplicity occurs (you may output any such value if multiple solutions exist).
'''
import os
import sys
from decimal import Decimal

def ProteinWeightDict():
    with open(os.path.join(os.path.dirname(__file__), 'protein_mass_table.txt')) as input_data:
        protein_weight_dict = {line.strip().split()[0]:float(line.strip().split()[1]) for line in input_data.readlines()}

    return protein_weight_dict

def get_weight(prot):
    w = 0
    for p in prot:
        w += ProteinWeightDict()[p]
    return w

with open(sys.argv[1]) as input_data:
    n = int(input_data.readline())
    protein = [input_data.readline().strip() for repeat in range(n)]
    weights = sorted([Decimal(line.strip()) for line in input_data.readlines()])

max_mult = -1
for p in protein:
    current_weights = sorted([Decimal(get_weight(item)) for i in range(1, len(p)) for item in (p[i:],p[:-i])] + [Decimal(get_weight(p))])
    multiset = dict()
    for cur in current_weights:
        for given in weights:
            if round(cur - given, 3) not in multiset:
                multiset[round(cur - given, 3)] = 1
            else:
                multiset[round(cur - given, 3)] += 1
    
    current_mult = max(multiset.values())

    if current_mult > max_mult:
        max_mult = current_mult
        max_protein = p

max_parameters = [str(max_mult), max_protein]

print ('\n'.join(max_parameters))
with open('submit.txt', 'w') as output_data:
    output_data.write('\n'.join(max_parameters))

#Ali Razzak