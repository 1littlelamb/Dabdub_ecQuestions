#Dabdub Problem 2013

import numpy as np

matrix_heatmap = [[0,0,0],
		     [0,0,0],
		     [0,0,0],
		     [0,0,0]]

matrix= [[0,0,0],
		 [0,0,0],
		 [0,0,0],
		 [0,0,0]]

final_matrix = [[0,0,0],
		  		[0,0,0],
		  		[0,0,0],
		  		[0,0,0]]

black_knights = [1,1,1]
white_knights = [2,2,2]

matrix[0] = black_knights
matrix[-1] = white_knights

final_matrix[0] = white_knights
final_matrix[-1] = black_knights

for row in matrix:
    print(' '.join([str(elem) for elem in row]))

rows = len(matrix)
cols = len(matrix[0])

def move_selector(pos):

	if pos == '00':
		moves = ['12','21']
		move = moves[np.random.randint(2)]
	elif pos == '01':
		moves = ['20','22']
		move = moves[np.random.randint(2)]
	elif pos == '02':
		moves = ['10','21']
		move = moves[np.random.randint(2)]
	elif pos == '10':
		moves = ['02','22','31']
		move = moves[np.random.randint(3)]
	elif pos == '11':
		moves = ['30','32']
		move = moves[np.random.randint(2)]
	elif pos == '12':
		moves = ['00','20','31']
		move = moves[np.random.randint(3)]
	elif pos == '20':
		moves = ['01','12','32']
		move = moves[np.random.randint(3)]
	elif pos == '21':
		moves = ['00','02']
		move = moves[np.random.randint(2)]
	elif pos == '22':
		moves = ['01','10','30']
		move = moves[np.random.randint(3)]
	elif pos == '30':
		moves = ['11','22']
		move = moves[np.random.randint(2)]
	elif pos == '31':
		moves = ['10','12']
		move = moves[np.random.randint(2)]
	elif pos == '32':
		moves = ['20','11']
		move = moves[np.random.randint(2)]
	else:
		move = [69]

	new_row, new_col = int(move[0]), int(move[1])

	return new_row, new_col

k = 0
while not np.array_equal(matrix, final_matrix):

	row = np.random.randint(4)
	col = np.random.randint(3)

	if matrix[row][col] in [1,2]:
		
		new_row, new_col = move_selector(str(row) + str(col))

		if matrix[new_row][new_col] not in [1,2]:
			matrix[row][col], matrix[new_row][new_col] = matrix[new_row][new_col], matrix[row][col]
			for i in range(len(matrix)):
				for j in range(len(matrix[0])):
					if matrix[i][j] in [1,2]:
						matrix_heatmap[i][j] += 1
			k+=1
			print(k)
			if k == 100:
				k = 0
				print('\n')
				for row in matrix_heatmap:
					print(' '.join([str(elem) for elem in row]))
				print('\n')	

			print('\n')
			for row in matrix:
				print(' '.join([str(elem) for elem in row]))
			print('\n')

	input()

print('DONE')