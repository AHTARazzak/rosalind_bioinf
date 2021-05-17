'''
Title: Creating a Restriction Map
Rosalind ID: PDPL
URL: http://rosalind.info/problems/pdpl
Goal: A set X containing n nonnegative integers such that ΔX=L.
'''
from collections import Counter
import sys

def partial_digest(distances):
    X = {0}
    width = max(distances)

    new_dist = lambda y, S: Counter(abs(y-s) for s in S)
    containment = lambda a, b: all(a[x] <= b[x] for x in a)

    while len(distances) > 0:
        y = max(distances)
        if containment(new_dist(y, X), distances):
            X |= {y}
            distances -= new_dist(y, X)
        else:
            X |= {width - y}
            distances -= new_dist(width - y, X)

    return X


def main():
    with open(sys.argv[1]) as input_data:
        distances = Counter(map(int,input_data.read().strip().split()))

    X = sorted(list(partial_digest(distances)))

    with open('submit.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, X)))

main()

#Ali Razzak