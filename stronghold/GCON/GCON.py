'''
Title: Global Alignment with Constant Gap Penalty
Rosalind ID: GCON
URL: http://rosalind.info/problems/gcon
Goal: The maximum alignment score between s and t. Use:
'''
import urllib
import contextlib
import sys
import os
from numpy import zeros

class BLOSUM62(object):
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), 'BLOSUM62.txt')) as input_data:
            items = [line.strip().split() for line in input_data.readlines()]
            self.scoring_matrix = {(item[0], item[1]):int(item[2]) for item in items}

    def __getitem__(self, pair):
        return self.scoring_matrix[pair[0], pair[1]]

def ReadFASTA(data_location):
        if type(data_location) == list:
                fasta_list = list()
                for location in data_location:
                        fasta_list+=ReadFASTA(location)
                return fasta_list

        if data_location[-4:] == '.txt':
                with open(data_location) as f:
                        return ParseFASTA(f)
        
        elif data_location[0:4] == 'http':
                with contextlib.closing(urllib.urlopen(data_location)) as f:
                        return ParseFASTA(f)


def ParseFASTA(f):
        fasta_list = list()
        for line in f:
                if line[0] == '>':
                        try:
                                fasta_list.append(current_dna)
                        except UnboundLocalError:
                                pass
                        current_dna = [line.lstrip('>').rstrip('\n'),'']

                else:
                        current_dna[1] += line.rstrip('\n')
        
        fasta_list.append(current_dna)

        return fasta_list

def global_alignment_with_constant_gap(v, w, scoring_matrix, sigma):

    S_lower = zeros((len(v)+1, len(w)+1), dtype=int)
    S_middle = zeros((len(v)+1, len(w)+1), dtype=int)
    S_upper = zeros((len(v)+1, len(w)+1), dtype=int)

    for i in range(1, len(v)+1):
        S_lower[i][0] = -sigma
        S_middle[i][0] = -sigma
        S_upper[i][0] = -10*sigma
    for j in range(1, len(w)+1):
        S_upper[0][j] = -sigma
        S_middle[0][j] = -sigma
        S_lower[0][j] = -10*sigma

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            S_lower[i][j] = max([S_lower[i-1][j], S_middle[i-1][j] - sigma])
            S_upper[i][j] = max([S_upper[i][j-1], S_middle[i][j-1] - sigma])
            S_middle[i][j] = max([S_lower[i][j], S_middle[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], S_upper[i][j]])

    max_score = S_middle[len(v)][len(w)]

    return max_score

if __name__ == '__main__':
    s, t = [fasta[1] for fasta in ReadFASTA(sys.argv[1])]

    score = str(global_alignment_with_constant_gap(s, t, BLOSUM62(), 5))

    print (score)
    with open('submit.txt', 'w') as output_data:
        output_data.write(score)
        
#Ali Razzak