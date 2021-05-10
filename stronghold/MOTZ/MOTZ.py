'''
Title: Motzkin Numbers and RNA Secondary Structures
Rosalind ID: MOTZ
URL: http://rosalind.info/problems/motz
Goal: The total number of noncrossing matchings of basepair edges in the bonding graph of s, modulo 1,000,000.
'''
from Bio import SeqIO
import sys

def _get_motzkin_numbers(s, n, motzkin_memo):
    if n <= 1:
        return 1
    if motzkin_memo.get((s, n),0):
        return motzkin_memo[(s, n)]
    cn = _get_motzkin_numbers(s[1:], n-1, motzkin_memo)
    for k in range(1, n):
        if (s[0], s[k]) in [("A", "U"), ("U", "A"), ("C", "G"), ("G", "C")]:
            cn += _get_motzkin_numbers(s[1:k], k-1, motzkin_memo) * _get_motzkin_numbers(s[k+1:], n-k-1, motzkin_memo)
    motzkin_memo[(s, n)] = cn
    return cn

seq_name, seq_string = [], []
with open (sys.argv[1],'r') as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

s = seq_string[0]
print(s)
nodes = len(s)
motzkin_memo = {}
motzkin_number= _get_motzkin_numbers(s, nodes, motzkin_memo)
print("catalan number: {}".format(motzkin_number))
print("modulo 1,000,000: {}".format(motzkin_number%1000000))

#Ali Razzak