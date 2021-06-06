'''
Title: Counting Optimal Alignments
Rosalind ID: CTEA
URL: http://rosalind.info/problems/ctea
Goal: The total number of optimal alignments of s and t with respect to edit alignment score, modulo 134,217,727 (227-1).
'''
import os
import sys
import urllib
import contextlib
from numpy import zeros

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

def count_alignment(v, w):
    S = zeros((len(v)+1, len(w)+1), dtype=int)
    dynamic_count = zeros((len(v)+1, len(w)+1), dtype=int)
    modulus = 2**27 - 1  # It may be a good idea to only compute this once...
    for i in range(0, len(v)+1):
        S[i][0] = i
        dynamic_count[i][0] = 1
    for j in range(1, len(w)+1):
        S[0][j] = j
        dynamic_count[0][j] = 1

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            scores = [S[i-1][j-1] + (v[i-1] != w[j-1]), S[i-1][j]+1, S[i][j-1]+1]
            S[i][j] = min(scores)

            dynamic_count[i][j] += [0, dynamic_count[i-1][j-1]][scores[0] == S[i][j]]
            dynamic_count[i][j] += [0, dynamic_count[i-1][j]][scores[1] == S[i][j]]
            dynamic_count[i][j] += [0, dynamic_count[i][j-1]][scores[2] == S[i][j]]

            dynamic_count[i][j] = dynamic_count[i][j] % modulus

    return dynamic_count[len(v)][len(w)]

if __name__ == '__main__':

    s, t = [fasta[1] for fasta in ReadFASTA(sys.argv[1])]

    count = str(count_alignment(s, t))

    print (count)
    with open('submit.txt', 'w') as output_data:
        output_data.write(count)

#Ali Razzak