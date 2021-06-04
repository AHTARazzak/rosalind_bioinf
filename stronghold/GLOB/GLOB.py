'''
Title: Global Alignment with Scoring Matrix
Rosalind ID: GLOB
URL: http://rosalind.info/problems/glob
Goal: The maximum alignment score between s and t. Use:
'''
import sys
from itertools import product
from Bio.SubsMat.MatrixInfo import blosum62
from Bio import SeqIO

def get_max_alignment(s, t):
    sl, tl = len(s), len(t)
    m = {(0, 0): (0, None)}
    m.update({((i, 0), (i * - 5, (i - 1, 0))) for i in range(1, sl + 1)})
    m.update({((0, i), (i * - 5, (0, i - 1))) for i in range(1, tl + 1)})
    
    for i, j in product(range(1, sl + 1), range(1, tl + 1)):
        cost = blosum62.get((s[i - 1], t[j - 1]))
        
        if cost == None:
            cost = blosum62.get((t[j - 1], s[i - 1]))
        d = m[(i - 1, j - 1)][0] + cost
        l = m[(i - 1, j)][0] - 5
        u = m[(i, j - 1)][0] - 5
        b = max(d, l, u)
        
        if d == b:
            m[(i, j)] = (b, (i - 1, j - 1))
        elif l == b:
            m[(i, j)] = (b, (i - 1, j))
        elif u == b:
            m[(i, j)] = (b, (i, j - 1))
            
    return (m[(i, j)][0])
    
if __name__ == '__main__':
    sequence_string = list()

    with open (sys.argv[1],'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            sequence_string.append(str(seq_record.seq))
    
    print (get_max_alignment(sequence_string[0], sequence_string[1]))
    

#Ali Razzak