'''
Title: Maximizing the Gap Symbols of an Optimal Alignment
Rosalind ID: MGAP
URL: http://rosalind.info/problems/mgap
Goal: The maximum number of gap symbols that can appear in any maximum score alignment of s and t with score parameters satisfying m>0, d<0, and g<0.
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

def maximum_gap_symbols(v, w):
    M = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    for i in range(len(v)):
        for j in range(len(w)):
            if v[i] == w[j]:
                M[i+1][j+1] = M[i][j]+1
            else:
                M[i+1][j+1] = max(M[i+1][j],M[i][j+1])

    return len(v) + len(w) - 2*M[len(v)][len(w)]


def main():
    v, w = [fasta[1] for fasta in ReadFASTA(sys.argv[1])]

    max_gaps = str(maximum_gap_symbols(v,w))

    print (max_gaps)
    with open('submit.txt', 'w') as output_data:
        output_data.write(max_gaps)

if __name__ == '__main__':
    main()

#Ali Razzak