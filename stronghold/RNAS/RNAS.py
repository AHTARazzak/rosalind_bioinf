'''
Title: Wobble Bonding and RNA Secondary Structures
Rosalind ID: RNAS
URL: http://rosalind.info/problems/rnas
Goal: The total number of distinct valid matchings of basepair edges in the bonding graph of s. Assume that wobble base pairing is allowed.
'''
from scipy.special import comb
import sys

def _get_bonding_graph(s, wobble_memo):
    if len(s) <= 3:
        return 1
    if s in wobble_memo:
        return wobble_memo[s]
    n = _get_bonding_graph(s[1:], wobble_memo)
    for i in range(4, len(s)):
            if (s[0], s[i]) in [("A", "U"), ("U", "A"), ("C", "G"), ("G", "C"), ("U", "G"), ("G", "U")]:
                n += _get_bonding_graph(s[1:i], wobble_memo) * _get_bonding_graph(s[i+1:], wobble_memo)
    wobble_memo[s] = n
    return n

the_sequence=open(sys.argv[1],"r").readlines()[0].strip()
print(the_sequence)
wobble_memo = {}
n = _get_bonding_graph(the_sequence, wobble_memo)
print(n)

#Ali Razzak