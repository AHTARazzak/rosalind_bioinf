the_fib_file = input("Name of file please: ")

fib_file = open(the_fib_file, 'r')

the_fib = fib_file.read().split()

n = int(the_fib[0])
k = int(the_fib[1])

fib_sequence = []

for i in range(n):
	if i < 2:
		fib_sequence.append(1)
	else:
		fib_sequence.append(fib_sequence[i-1] + (fib_sequence[i-2])*k)
print(fib_sequence[-1])