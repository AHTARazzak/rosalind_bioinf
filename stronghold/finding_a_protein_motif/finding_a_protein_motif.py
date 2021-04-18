import sys
import requests
import re
from bs4 import BeautifulSoup

search_proteins =  open(sys.argv[1], "r")
read_proteins = search_proteins.read().split()

out_file = open("to_submit.txt", "a")

fasta_pull_list = []

for protein in read_proteins:
	URL = "http://www.uniprot.org/uniprot/" + protein + ".fasta"
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	sequence_only = "".join(str(soup).split("\n")[1:])
	index_list = ([m.start() for m in re.finditer(r"(?=(N(H|G|K|Q|D|E|F|S|M|R|L|I|V|T|Y|W|C|V|A|N|U)(S|T)(H|K|Q|D|E|F|S|M|R|L|I|V|T|Y|W|C|V|A|N|U|G)))", sequence_only)])
	string_list = ""
	if len(index_list) > 0:
		for index in index_list:
			string_list += str(index +1) + " "
		out_file.write(protein + "\n")
		out_file.write(string_list[:-1] + "\n")
