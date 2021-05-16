'''
Title: Creating a Character Table
Rosalind ID: CTBL
URL: http://rosalind.info/problems/ctbl
Goal: A character table having the same splits as the edge splits of T. The columns of the character table should encode the taxa ordered lexicographically; the rows of the character table may be given in any order. Also, for any given character, the particular subset of taxa to which 1s are assigned is arbitrary.
'''
import sys
from numpy import zeros

class Node(object):
    def __init__(self, number, parent, name=None):
        self.number = number
        self.parent = parent
        self.children = []
        self.name = [name, 'Node_' + str(self.number)][name is None]

    def __repr__(self):
        return ['Node_' + str(self.number) + '('+str(self.name)+')', str(self.name)+'()'][self.name == 'Node_'+str(self.number)]

    def add_child(self, child):
        self.children.append(child)


class Newick(object):
    def __init__(self, data):
        self.nodes = []
        self.node_index = 0
        self.edges = []
        self.construct_tree(data)
        self.name_index = {node.name: node.number for node in self.nodes}

    def construct_tree(self, data):
        data = data.replace(',', ' ').replace('(','( ').replace(')',' )').strip(';').split()
        current_parent = Node(-1, None)
        for item in data:
            if item[0] == '(':
                current_parent = Node(len(self.nodes), current_parent.number)
                self.nodes.append(current_parent)
                if len(self.nodes) > 1:
                    self.nodes[current_parent.parent].add_child(current_parent.number)
                    self.edges.append((current_parent.parent, current_parent.number))

            elif item[0] == ')':
                if len(item) > 1:
                    current_parent.name = item[1:]
                current_parent = self.nodes[current_parent.parent]

            else:
                self.nodes[current_parent.number].add_child(len(self.nodes))
                self.edges.append((current_parent.number, len(self.nodes)))
                self.nodes.append(Node(len(self.nodes), current_parent.number, item))

    def edge_names(self):
        return [(self.nodes[edge[0]].name, self.nodes[edge[1]].name) for edge in self.edges]

    def distance(self, name1, name2):
        if name1 == name2:
            return 0

        branch1 = [self.name_index[name1]]
        branch2 = [self.name_index[name2]]
        while self.nodes[branch1[-1]].parent != -1:
            branch1.append(self.nodes[branch1[-1]].parent)
        while self.nodes[branch2[-1]].parent != -1:
            branch2.append(self.nodes[branch2[-1]].parent)

        return len(set(branch1) ^ set(branch2)) + 1

    def get_descendants(self, node_name):
        descendants = []
        for child in self.nodes[self.name_index[node_name]].children:
            descendants.append(self.nodes[child].name)
            descendants += self.get_descendants(self.nodes[child].name)

        return descendants

with open(sys.argv[1]) as input_data:
    newick_input = input_data.read().strip()

newick_tree = Newick(newick_input)

named_nodes = lambda n: 'Node_' not in n
unnamed_edges = lambda e: 'Node_' in e[0] and 'Node_' in e[1]

node_order = {name:index for index,name in enumerate(sorted(filter(named_nodes, [node.name for node in newick_tree.nodes])))}

nontrivial_edges = filter(unnamed_edges, newick_tree.edge_names())

M = zeros((len(list(nontrivial_edges)), len(list(node_order))), dtype=int)
for i, edge in enumerate(nontrivial_edges):
    taxa = filter(named_nodes, set(newick_tree.get_descendants(edge[0])) & set(newick_tree.get_descendants(edge[1])))
    for t in taxa:
        M[i][node_order[t]] = 1

with open('submit.txt', 'w') as output_data:
    output_data.write('\n'.join([''.join(map(str, M[i])) for i in range(len(M))]))

#Ali Razzak

