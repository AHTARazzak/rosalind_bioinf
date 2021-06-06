'''
Title: Local Alignment with Affine Gap Penalty
Rosalind ID: LAFF
URL: http://rosalind.info/problems/laff
Goal: The maximum local alignment score of s and t, followed by substrings r and u of s and t, respectively, that correspond to the optimal local alignment of s and t. Use:
'''
import os
import sys
import urllib
import contextlib

class BLOSUM62(object):

    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), 'BLOSUM62.txt')) as input_data:
            items = [line.strip().split() for line in input_data.readlines()]
            self.scoring_matrix = {(item[0], item[1]):int(item[2]) for item in items}

    def __getitem__(self, pair):
        return self.scoring_matrix[pair[0], pair[1]]


def ReadFASTA(data_location):
        if type(data_location) == list:
                fasta_list =[]
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
        fasta_list=[]
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

def local_alignment_affine_gap_penalty(v, w, scoring_matrix, sigma, epsilon):
    S_lower = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    S_middle = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    S_upper = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    backtrack = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]

    max_score = -1
    max_i, max_j = 0, 0

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            S_lower[i][j] = max([S_lower[i-1][j] - epsilon, S_middle[i-1][j] - sigma])
            S_upper[i][j] = max([S_upper[i][j-1] - epsilon, S_middle[i][j-1] - sigma])
            middle_scores = [S_lower[i][j], S_middle[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], S_upper[i][j], 0]
            S_middle[i][j] = max(middle_scores)
            backtrack[i][j] = middle_scores.index(S_middle[i][j])

            if S_middle[i][j] > max_score:
                max_score = S_middle[i][j]
                max_i, max_j = i, j

    i, j = max_i, max_j

    v_aligned, w_aligned = v[:i], w[:j]

    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
        elif backtrack[i][j] == 1:
            i -= 1
            j -= 1
        elif backtrack[i][j] == 2:
            j -= 1

    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return str(max_score), v_aligned, w_aligned


if __name__ == '__main__':

    s, t = [fasta[1] for fasta in ReadFASTA(sys.argv[1])]

    alignment = local_alignment_affine_gap_penalty(s, t, BLOSUM62(), 11, 1)

    print ('\n'.join(alignment))
    with open('submit.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))