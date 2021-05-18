'''
Title: Linguistic Complexity of a Genome
Rosalind ID: LING
URL: http://rosalind.info/problems/ling
Goal: The linguistic complexity lc(s).
'''
import sys
from math import log

class SuffixTree(object):
    def __init__(self, word):
        self.nodes = [self.Node(None, 0)]
        self.edges = dict()
        self.descendants_dict = dict()
        if type(word) == str:
            self.add_word(word)

    class Node(object):
        def __init__(self, parent, number):
            self.parent = parent
            self.number = number
            self.children = []

        def add_child(self, child):
            self.children.append(child)

        def remove_child(self, child):
            self.children.remove(child)

        def update_parent(self, parent):
            self.parent = parent

    def add_word(self, word):
        if word[-1] != '$':
            word += '$'
        self.word = word
        self.n = len(self.word)

        for i in range(self.n):
            parent_node, edge_start, overlap = self.insert_position(i, self.nodes[0])

            if overlap:
                p_edge_start, p_edge_end = self.edges[(parent_node.parent.number, parent_node.number)]

                insert_len = 0
                while word[edge_start:edge_start + insert_len] == word[p_edge_start:p_edge_start + insert_len]:
                    insert_len += 1

                new_node = self.Node(parent_node.parent, len(self.nodes))
                new_node.add_child(parent_node)
                self.add_node(parent_node.parent, p_edge_start, p_edge_start + insert_len - 1, new_node)

                del self.edges[(parent_node.parent.number, parent_node.number)]
                parent_node.parent.remove_child(parent_node)
                parent_node.update_parent(new_node)
                self.edges[(parent_node.parent.number, parent_node.number)] = [p_edge_start + insert_len - 1, p_edge_end]

                self.add_node(new_node, edge_start + insert_len - 1, self.n)

            else:
                self.add_node(parent_node, edge_start, self.n)

    def insert_position(self, start_index, parent_node):
        for child_node in parent_node.children:
            edge_start, edge_end = self.edges[(parent_node.number, child_node.number)]
            if self.word[start_index:start_index + edge_end - edge_start] == self.word[edge_start:edge_end]:
                return self.insert_position(start_index + edge_end - edge_start, child_node)

            elif self.word[edge_start] == self.word[start_index]:
                return child_node, start_index,  True

        return parent_node, start_index, False

    def add_node(self, parent_node, edge_start, edge_end, child_node=None):
        if child_node is None:
            child_node = self.Node(parent_node, len(self.nodes))

        self.nodes.append(child_node)

        parent_node.add_child(child_node)

        self.edges[(parent_node.number, child_node.number)] = [
            edge_start, edge_end]

    def print_edges(self):
        return [self.word[i:j] for i, j in self.edges.values()]

    def total_descendants(self, base_node):
        if base_node not in self.descendants_dict:
            self.descendants_dict[base_node] = len(base_node.children) + sum([self.total_descendants(c) for c in base_node.children])

        return self.descendants_dict[base_node]

    def node_word(self, end_node):
        current_word = ''
        while end_node.number != 0:
            temp_indices = self.edges[(end_node.parent.number, end_node.number)]
            current_word = self.word[temp_indices[0]:temp_indices[1]] + current_word
            end_node = end_node.parent

        return current_word.strip('$')

with open(sys.argv[1]) as input_data:
    dna = input_data.read().strip()
    n = len(dna)

edges = [edge if edge[1] != n+1 else [edge[0], n] for edge in SuffixTree(dna).edges.values()]
sub = float(sum([edge[1]-edge[0] for edge in edges]))

m = float(sum([n-k+1 if k > log(n+1)/log(4) else 4**k for k in range(1, n+1)]))  # log's and if statement to avoid 4^k when k large.

with open('submit.txt', 'w') as output_file:
    output_file.write(str(sub/m))

# Ali Razzak