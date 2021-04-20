from Bio.Seq import Seq

the_rna_file = input("Name of file please: ")
rna_file = open(the_rna_file, 'r')
the_rna = rna_file.read()

rna = Seq(the_rna)
print(str(rna.translate(to_stop=True)))