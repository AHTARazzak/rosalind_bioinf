'''
Title: Multiple Alignment
Rosalind ID: MULT
URL: http://rosalind.info/problems/mult
Goal: A multiple alignment of the strings having maximum score, where we score matched symbols 0 (including matched gap symbols) and all mismatched symbols -1 (thus incorporating a linear gap penalty of 1).
'''
import sys
from itertools import product
from operator import add, mul
from scipy.special import comb
import urllib
import contextlib
import functools

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

def multiple_alignment(word_list):
    word_list = ['$'+word for word in word_list]
    S, backtrack = dict(), dict()
    perm_list = list(product([0, -1], repeat=len(word_list)))[1:]
    base_score = -1*comb(len(word_list), 2, exact=True)

    for index in product(*map(range,map(lambda s: len(s) + 1, word_list))):

        if functools.reduce(mul, index) == 0:
            if sum(index) == 0:
                S[index] = 0
            else:
                S[index] = 2*base_score*functools.reduce(add, map(len, word_list))

        else:
            previous_scores = [S[tuple(map(add, index, perm))] for perm in perm_list]
            current_index_scores = list()
            for perm in perm_list:
                chars = [word_list[i][index[i]-1] if perm_value == -1 else '-' for i, perm_value in enumerate(perm)]
                current_index_scores.append(base_score + sum([comb(chars.count(ch), 2, exact=True) for ch in set(chars)]))

            scores = map(add, previous_scores, current_index_scores)
            backtrack[index], S[index] = max(enumerate(scores), key=lambda p: p[1])

    alignment = word_list
    current_index = map(len, word_list)

    max_score = S[tuple(current_index)]

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    while functools.reduce(mul, current_index) != 0:
        for i, perm_value in enumerate(perm_list[backtrack[tuple(current_index)]]):
            if perm_value == 0:
                alignment[i] = insert_indel(alignment[i], current_index[i])
            else:
                current_index[i] -= 1

    return [str(max_score)] + [aligned[1:] for aligned in alignment]


if __name__ == '__main__':

    words = [fasta[1] for fasta in ReadFASTA(sys.argv[1])]

    words_aligned = multiple_alignment(words)

    # Print and save the answer.
    print ('\n'.join(words_aligned))
    with open('submit.txt', 'w') as output_data:
        output_data.write('\n'.join(words_aligned))
#Ali Razzak

