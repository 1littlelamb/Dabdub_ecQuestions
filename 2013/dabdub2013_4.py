#Dabdub Problem 2013

from treelib import Tree, Node
import numpy as np
import pandas as pd
from tqdm import tqdm

matrix = np.array([[0,0,0],
				   [0,0,0],
				   [0,0,0],
				   [0,0,0]])

final_matrix = matrix.copy()

black_knights = np.array([11,12,13])
white_knights = np.array([21,22,23])

matrix[0] = black_knights
matrix[-1] = white_knights

final_matrix[0] = white_knights
final_matrix[-1] = black_knights

alphabet = 'abcdefghijklmnopqrstuvwxyz'

tree = Tree()
tree.create_node(('1' + alphabet[0]), alphabet[0], parent=None, data=matrix)

def move_selector(pos):

	if pos == '00':
		moves = ['12','21']
		pass
	elif pos == '01':
		moves = ['20','22']
		pass
	elif pos == '02':
		moves = ['10','21']
		pass
	elif pos == '10':
		moves = ['02','22','31']
		pass
	elif pos == '11':
		moves = ['30','32']
		pass
	elif pos == '12':
		moves = ['00','20','31']
		pass
	elif pos == '20':
		moves = ['01','12','32']
		pass
	elif pos == '21':
		moves = ['00','02']
		pass
	elif pos == '22':
		moves = ['01','10','30']
		pass
	elif pos == '30':
		moves = ['11','22']
		pass
	elif pos == '31':
		moves = ['10','12']
		pass
	elif pos == '32':
		moves = ['20','11']
		pass

	return moves

exit_ = False
trsh_bin = 0
while not exit_:
	
	level_ = str(tree.depth())
	print('Level: ' + level_)
	print('Trashed ' + str(trsh_bin) + ' branches so far')
	if level_ == '24':
		break
	ids_ = [node.identifier for node in tree.leaves()]
	for id_parent in tqdm(ids_):					   								   #Here we iterate through all the leaves of our tree, creating an ever
		parent_matrix = tree[id_parent].data										   # more complex tree structure
		child_matrix = parent_matrix.copy()
		i=0
		for row in range(parent_matrix.shape[0]):                                      #Iterating across every matrix cell
			for col in range(parent_matrix.shape[1]):
				if parent_matrix[row][col] != 0:                                       #Checking if peice
					moves = move_selector(str(row) + str(col))                         #Aquiring moves from the move_selector(), ended up being like a washed _dict
					for move in moves:
						new_row, new_col = int(move[0]), int(move[1])                  #Extracting the move info from the _str class 
						if parent_matrix[new_row][new_col] == 0:
							child_matrix[row][col], child_matrix[new_row][new_col] =\
							child_matrix[new_row][new_col], child_matrix[row][col]     #Conducting the move
							id_child = id_parent + alphabet[i]                         #Creating the id
							try:
								if not np.array_equal(child_matrix, tree[id_parent[:-1]].data):
									tree.create_node((level_ + id_child), id_child,\
													  parent=id_parent, data=child_matrix) #Adding the new board to the tree
								else:
									trsh_bin+=1
							except:
								tree.create_node((level_ + id_child), id_child,\
												  parent=id_parent, data=child_matrix)
							child_matrix = parent_matrix.copy()						   #Refreshing the child for the next loop
							i+=1
						if np.array_equal(child_matrix, final_matrix):
							exit_ = True

print('DONE')