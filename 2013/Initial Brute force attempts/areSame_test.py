matrix = [[0,0,0],
		  [0,0,0],
		  [0,0,0],
		  [0,0,0]]

final_matrix = matrix.copy()
black_knights = [11,12,13]
white_knights = [21,22,23]

matrix[0] = black_knights
matrix[-1] = white_knights

final_matrix[0] = white_knights
final_matrix[-1] = black_knights

def areSame(A,B):

	for i in range(4):
		for j in range(3):
			if (A[i][j] != B[i][j]):
				return 0
	return 1

print(areSame(matrix, matrix))