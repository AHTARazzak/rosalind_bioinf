contigs <- scan('rosalind_asmq.txt', what='character')
lengths <- nchar(contigs)
L <- seq(max(lengths),min(lengths), -1)

N <- vector(mode='numeric', length=length(L))
N[1] = L[1]*length(lengths[lengths==L[1]])
for(i in 2:length(L) ){
  N[i] = L[i]*length(lengths[lengths==L[i]]) + N[i-1]
}

minL <- c(ceiling(0.5*sum(lengths)),ceiling(0.75*sum(lengths)))
N_values <- vector(mode='numeric', length=2)
for (i in 1:2){
  N_values[i] = L[match(min(N[N>minL[i]]),N)]
}

cat(as.character(N_values), file='submit.txt', sep=' ')