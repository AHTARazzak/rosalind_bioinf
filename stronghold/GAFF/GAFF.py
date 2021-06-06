'''
Title: Global Alignment with Scoring Matrix and Affine Gap Penalty
Rosalind ID: GAFF
URL: http://rosalind.info/problems/gaff
Goal: The maximum alignment score between s and t, followed by two augmented strings s′ and t′ representing an optimal alignment of s and t. Use:
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


def global_alignment_affine_gap_penalty(v, w, scoring_matrix, sigma, epsilon):
    S = [[[0 for j in range(len(w)+1)] for i in range(len(v)+1)] for k in range(3)]
    backtrack = [[[0 for j in range(len(w)+1)] for i in range(len(v)+1)] for k in range(3)]

    for i in range(1, len(v)+1):
        S[0][i][0] = -sigma - (i-1)*epsilon
        S[1][i][0] = -sigma - (i-1)*epsilon
        S[2][i][0] = -10*sigma
    for j in range(1, len(w)+1):
        S[2][0][j] = -sigma - (j-1)*epsilon
        S[1][0][j] = -sigma - (j-1)*epsilon
        S[0][0][j] = -10*sigma

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            lower_scores = [S[0][i-1][j] - epsilon, S[1][i-1][j] - sigma]
            S[0][i][j] = max(lower_scores)
            backtrack[0][i][j] = lower_scores.index(S[0][i][j])

            upper_scores = [S[2][i][j-1] - epsilon, S[1][i][j-1] - sigma]
            S[2][i][j] = max(upper_scores)
            backtrack[2][i][j] = upper_scores.index(S[2][i][j])

            middle_scores = [S[0][i][j], S[1][i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], S[2][i][j]]
            S[1][i][j] = max(middle_scores)
            backtrack[1][i][j] = middle_scores.index(S[1][i][j])

    i,j = len(v), len(w)
    v_aligned, w_aligned = v, w

    matrix_scores = [S[0][i][j], S[1][i][j], S[2][i][j]]
    max_score = max(matrix_scores)
    backtrack_matrix = matrix_scores.index(max_score)

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    while i*j != 0:
        if backtrack_matrix == 0:
            if backtrack[0][i][j] == 1:
                backtrack_matrix = 1
            i -= 1
            w_aligned = insert_indel(w_aligned, j)

        elif backtrack_matrix == 1:
            if backtrack[1][i][j] == 0:
                backtrack_matrix = 0
            elif backtrack[1][i][j] == 2:
                backtrack_matrix = 2
            else:
                i -= 1
                j -= 1

        else:
            if backtrack[2][i][j] == 1:
                backtrack_matrix = 1
            j -= 1
            v_aligned = insert_indel(v_aligned, i)

    for _ in range(i):
        w_aligned = insert_indel(w_aligned, 0)
    for _ in range(j):
        v_aligned = insert_indel(v_aligned, 0)

    return str(max_score), v_aligned, w_aligned


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

def main():
    s, t = [fasta[1] for fasta in ReadFASTA(sys.argv[1])]

    score = global_alignment_affine_gap_penalty(s, t, BLOSUM62(), 11, 1)

    print ('\n'.join(score))
    with open('submit.txt', 'w') as output_data:
        output_data.write('\n'.join(score))

if __name__ == '__main__':
    main()