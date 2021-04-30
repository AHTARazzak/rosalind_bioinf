'''
Title: Mortal Fibonacci Rabbits
Rosalind ID: FIBD
URL: http://rosalind.info/problems/fibd
Goal: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
'''

the_fib_file = input("Name of file please: ")
fib_file = open(the_fib_file, 'r')
the_fib = fib_file.read().split()

n = int(the_fib[0])
m = int(the_fib[1])

ages = [1] + [0] * (m - 1)
for i in range(n - 1):
	ages = [sum(ages[ 1 : ])] + ages[ : -1]
print(sum(ages))

#Ali Razzak