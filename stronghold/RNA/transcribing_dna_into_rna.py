nucleotide_allowed = ["A", "U", "G", "C"]

the_sequence_file = input("Name of file please: ")

sequence_file = open(the_sequence_file, 'r')

the_sequence = sequence_file.read()


converted_sequence = the_sequence.replace("T", "U")
print(converted_sequence)