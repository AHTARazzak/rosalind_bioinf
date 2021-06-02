#Title: Wright-Fisher's Expected Behavior
#Rosalind ID: EBIN
#URL: http://rosalind.info/problems/ebin
#Goal: An array B of length m for which B[k] is the expected value of Bin(n,P[k]); in terms of Wright-Fisher, it represents the expected allele frequency of the next generation.

n <- scan("rosalind_ebin.txt",nlines = 1)
p <- scan("rosalind_ebin.txt", skip = 1)
E <- n*p
cat(as.character(E), file='submit.txt', sep=' ')

#By Ali Razzak