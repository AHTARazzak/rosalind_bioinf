'''
Title: Inferring Genotype from a Pedigree
Rosalind ID: MEND
URL: http://rosalind.info/problems/mend
Goal: Three numbers between 0 and 1, corresponding to the respective probabilities that the individual at the root of T will exhibit the "AA", "Aa" and "aa" genotypes.
'''
import sys

prob_dict ={
            ("AA", "AA"): (1.0, 0.0, 0.0),
            ("AA", "Aa"): (0.5, 0.5, 0.0),    
            ("AA", "aa"): (0.0, 1.0, 0.0),
            ("Aa", "AA"): (0.5, 0.5, 0.0), 
            ("Aa", "Aa"): (0.25, 0.5, 0.25),
            ("Aa", "aa"): (0.0, 0.5, 0.5),
            ("aa", "AA"): (0.0, 1.0, 0.0),
            ("aa", "Aa"): (0.0, 0.5, 0.5),
            ("aa", "aa"): (0.0, 0.0, 1.0)
            }

def cp(ancestor1, ancestor2):
    p = {"AA":0.0, "Aa":0.0, "aa":0.0}
    for k1,v1 in ancestor1.items():
        for k2,v2 in ancestor2.items():
            p["AA"] += v1*v2*prob_dict[(k1,k2)][0]
            p["Aa"] += v1*v2*prob_dict[(k1,k2)][1]
            p["aa"] += v1*v2*prob_dict[(k1,k2)][2]
    return p

AA = {"AA":1.0, "Aa":0.0, "aa":0.0}
Aa = {"AA":0.0, "Aa":1.0, "aa":0.0}
aa = {"AA":0.0, "Aa":0.0, "aa":1.0}

with open(sys.argv[1], "r") as f:
    pedigree = f.readline().strip()
    pedigree = pedigree.replace(";", "").replace("(", "cp(")
    for key, value in eval(pedigree).items():
        print(value)
    #print(eval(pedigree))

#Ali Razzak