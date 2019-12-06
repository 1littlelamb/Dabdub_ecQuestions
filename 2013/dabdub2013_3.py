#Dabdub Problem 2013

from anytree import Node, RenderTree
import numpy as np
import pandas as pd

matrix = np.array([[0,0,0],
				   [0,0,0],
				   [0,0,0],
				   [0,0,0]])

final_matrix = matrix.copy()

black_knights = np.array([11,12,13])
white_knights = np.array([21,22,23])

print(black_knights)

matrix[0] = black_knights
matrix[-1] = white_knights

print(matrix)

final_matrix[0] = white_knights
final_matrix[-1] = black_knights

columns = ['child','parent']
tree = pd.DataFrame({'child':[matrix],'parent':[matrix]}, columns=columns)

print(tree.child.values)

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
quit()
k = 0
while True:
	parent_matrix = tree
	for k in range(3):	
		for row in range(matrix.shape[0]):
			for col in range(matrix.shape[1]):
				if matrix[row][col] != 0:
					
					moves = move_selector(str(row) + str(col))

					for move in moves:
						new_row, new_col = int(move[0]), int(move[1])

						if matrix[new_row][new_col] != 0:
							new_matrix = matrix.copy()
							matrix[row][col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[row][col]



			#if k == 100:
			#	k = 0
			#	print('\n')
			#	for row in matrix_heatmap:
			#		print(' '.join([str(elem) for elem in row]))
			#	print('\n')	

			#print('\n')
			#for row in matrix:
			#	print(' '.join([str(elem) for elem in row]))
			#print('\n')

			print(matrix)
	break





print('DONE')