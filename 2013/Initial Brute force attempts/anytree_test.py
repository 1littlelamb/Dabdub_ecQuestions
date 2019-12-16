from anytree import Node, RenderTree
import pandas as pd
import numpy as np
from treelib import Tree, Node

matrix= np.array([[0,0,0],
				  [0,0,0],
				  [0,0,0],
				  [0,0,0]])

#for i in range(matrix.shape[1]):
#	print(i)
#
#A = Node(matrix)
#B = Node(matrix, parent=A)
#C = Node(matrix, parent=A)
#
#for pre, fill, node in RenderTree(A):
#    print("%s%s" % (pre, node.name))
#
#
#tree = pd.DataFrame({'child':[matrix],'parent':[matrix]}, columns=['child','parent'])
#
#print(tree.parent[0])

#for i in range(len(tree.columns)):
#	for row in tree[columns[i]][0]:
#	    print(' '.join([str(elem) for elem in row]))

tree = Tree()
tree.create_node(matrix, '1a')

tree.create_node(matrix, '2a', parent='1a')


print(tree.depth(tree.get_node('2a')))

print([tree[node].tag for node in \
            tree.expand_tree(mode=Tree.DEPTH)])



tree2 = Tree()
tree2.create_node("Harry", "harry")  # root node
tree2.create_node("Jane", "jane", parent="harry")
tree2.create_node("Bill", "bill", parent="harry")
tree2.create_node("Diane", "diane", parent="harry")
tree2.create_node("Mary", "mary", parent="harry")
tree2.create_node("Mark", "mark", parent="harry")

for node in tree2.is_branch('harry'):
	print(tree2[node].data)

id_ = [node.identifier for node in tree2.leaves()]

tree2.remove_node('harry')

tree2.save2file('tree2.txt')

print(id_)

