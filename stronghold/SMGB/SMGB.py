'''
Title: Matching a Spectrum to a Protein
Rosalind ID: SMGB
URL: http://rosalind.info/problems/smgb
Goal: The maximum semiglobal alignment score of s and t, followed by an alignment of s and t achieving this maximum score. Use an alignment score in which matching symbols count +1, substitutions count -1, and there is a linear gap penalty of 1. If multiple optimal alignments exist, then you may return any one.
'''
from Bio import SeqIO
import sys

def get_empty_matrix(dimensions):
    retval = list()
    for _ in range(dimensions[0]):
        retval.append([])    
        for _ in range(dimensions[1]):
            retval[-1].append(0)
            
    return (retval)

def get_match_score(s, t):
    if s == t:
        return match_award
    elif s == '-' or t == '-':
        return gap_penalty
    else:
        return mismatch_penalty

def get_semiglobal_alignment(s, t):
    m = len(s)
    n = len(t)
    
    score = get_empty_matrix((n + 1, m + 1))
    
    for i in range(n+1) :
        score[i][0] = i*0
    
    for j in range(m+1) :
        score[0][j] = j*0
    
    pointer = get_empty_matrix((n+1, m+1))
    for i in range(n+1) :
        pointer[i][0] = 1
    for j in range(m+1) :
        pointer[0][j] = 2
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score_diagonal = score[i-1][j-1] + get_match_score(s[j-1], t[i-1])
            score_up = score[i][j-1] + gap_penalty
            score_left = score[i-1][j] + gap_penalty
            score[i][j] = max(score_left, score_up, score_diagonal)

            if score[i][j] == score_diagonal :
                pointer[i][j] = 3
            if score[i][j] == score_up :
                pointer[i][j] = 2
            if score[i][j] == score_left :
                pointer[i][j] = 1
    
    align1, align2 = str(), str()
    
    max_j = score[-1].index(max(score[-1]))
    print (max(score[-1]))
    
    while 1 :
        if j > max_j :
            align1 = s[j-1] + align1
            align2 = '-' + align2
            j -= 1
            continue
        if pointer[i][j] == 3 :
            align1 = s[j-1] + align1
            align2 = t[i-1] + align2
            i -= 1
            j -= 1
        elif pointer[i][j] == 2 :
            align2 = '-' + align2
            align1 = s[j-1] + align1
            j -= 1
        elif  pointer[i][j] == 1 :
            align2 = t[i-1] + align2
            align1 = '-' + align1
            i -= 1
        if (i == 0 and j == 0) : break
        
    return (align1 + '\n' + align2)

if __name__ == "__main__":
    dataset = list(SeqIO.parse(sys.argv[1], "fasta"))

    s = dataset[0].seq
    t = dataset[1].seq
    
    match_award = 1
    mismatch_penalty = -1
    gap_penalty = -1 
    outfile = open("subtmit.txt","w")
    outfile.write(get_semiglobal_alignment(s, t))

#Ali Razzak