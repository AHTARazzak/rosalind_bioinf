'''
Title: Finding a Motif with Modifications
Rosalind ID: SIMS
URL: http://rosalind.info/problems/sims
Goal: An optimal fitting alignment score with respect to the mismatch score defined above, followed by an optimal fitting alignment of a substring of s against t. If multiple such alignments exist, then you may output any one.
'''
import urllib
import contextlib
import sys

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

def fitting_alignment(v, w):
    S = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    backtrack = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]

    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            scores = [S[i-1][j] - 1, S[i][j-1] - 1, S[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    j = len(w)
    i = max(enumerate([S[row][j] for row in range(len(w), len(v))]),key=lambda x: x[1])[0] + len(w)
    max_score = S[i][j]

    v_aligned, w_aligned = v[:i], w[:j]

    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    v_aligned = v_aligned[i:]

    return str(max_score), v_aligned, w_aligned


def main():
    word1, word2 = [fasta[1] for fasta in ReadFASTA(sys.argv[1])]
    alignment = fitting_alignment(word1, word2)
    print ('\n'.join(alignment))
    with open('submit.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))

if __name__ == '__main__':
    main()

#Ali Razzak