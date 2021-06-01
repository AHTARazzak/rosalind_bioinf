'''
Title: Inferring Peptide from Full Spectrum
Rosalind ID: FULL
URL: http://rosalind.info/problems/full
Goal: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple solutions exist, you may output any one.
'''
import sys
import os

def ProteinWeightDict():
    with open(os.path.join(os.path.dirname(__file__), 'protein_mass_table.txt')) as input_data:
        protein_weight_dict = {line.strip().split()[0]:float(line.strip().split()[1]) for line in input_data.readlines()}

    return protein_weight_dict

def find_weight_match(current_w, w_list):
    for weight in w_list:
        for item in ProteinWeightDict().items():
            if abs(item[1] - (weight - current)) < 0.01:
                return item[0]

    return -1

if __name__ == '__main__':
    with open(sys.argv[1]) as input_data:
        weights = [float(line.strip()) for line in input_data.readlines()]

    n = (len(weights)-3)/2

    protein = str()
    current = weights[1]
    myw = [w for w in weights[2:]]

    while len(protein) < n:
        temp = find_weight_match(current, myw)
        if temp == -1:
            break
        else:
            protein += temp
            current += ProteinWeightDict()[temp]
            myw = filter(lambda w: w-current > 0, myw)

    with open('submit.txt', 'w') as output_file:
        output_file.write(protein)

#Ali Razzak