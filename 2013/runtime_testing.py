#testing crazy fucking long loop

import tqdm
import sys
import numpy as np
import timeit

#Numpy Integer 
xd_np = np.array([[1,0,0],
				  [0,0,0],
				  [0,0,0],
				  [0,0,0]])

np_int_test = '''
import numpy as np

xd_np = np.array([[1,0,0],
				  [0,0,0],
				  [0,0,0],
				  [0,0,0]])

for i in range(10000):
	xd_np[0][0], xd_np[3][2] = xd_np[3][2], xd_np[0][0]

'''

#Regular Integer
xd_reg = [[1,0,0],
		  [0,0,0],
		  [0,0,0],
		  [0,0,0]]

reg_int_test = '''

xd_reg = [[1,0,0],
		  [0,0,0],
		  [0,0,0],
		  [0,0,0]]

for i in range(10000):
	xd_reg[0][0], xd_reg[3][2] = xd_reg[3][2], xd_reg[0][0]

'''

#Numpy String
xs_np = np.array([['a','-','-'],
			   ['-','-','-'],
			   ['-','-','-'],
			   ['-','-','-']])

np_str_test = '''
import numpy as np

xs_np = np.array([['a','-','-'],
			   ['-','-','-'],
			   ['-','-','-'],
			   ['-','-','-']])

for i in range(10000):
	xs_np[0][0], xs_np[3][2] = xs_np[3][2], xs_np[0][0]

'''

#Regular String
xs_reg = [['a','-','-'],
		  ['-','-','-'],
		  ['-','-','-'],
		  ['-','-','-']]

reg_str_test = '''

xs_reg = [['a','-','-'],
		  ['-','-','-'],
		  ['-','-','-'],
		  ['-','-','-']]

for i in range(10000):
	xs_reg[0][0], xs_reg[3][2] = xs_reg[3][2], xs_reg[0][0]

'''

if_else_version = '''

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

for i in range(10000):
	moves = move_selector(str(np.random.randint(4)) + str(np.random.randint(3)))

'''

dict_version = '''

dict_py = {'00':['12','21'],'01':['20','22'],'02':['10','21'],'10':['02','22','31'],'11':['30','32'],'12':['00','20','31'],'20':['01','12','32'],'21':['00','02'],'22':['01','10','30'],'30':['11','22'],'31':['10','12'],'32':['20','11']}

for i in range(10000):
	moves = dict_py[str(np.random.randint(4)) + str(np.random.randint(3))]

'''

#Running the tests and timing
np_int_test_time = timeit.timeit(np_int_test, number=100)/100
reg_int_test_time = timeit.timeit(reg_int_test, number=100)/100
np_str_test_time = timeit.timeit(np_str_test, number=100)/100
reg_str_test_time = timeit.timeit(reg_str_test, number=100)/100

if_else_version_time = timeit.timeit(if_else_version, setup='import numpy as np', number=100)/100
dict_version_time = timeit.timeit(dict_version, setup='import numpy as np', number=100)/100

#Printing everything
print(' ')
print('Size of Numpy Digit matrix:  ' + str(sys.getsizeof(xd_np)))
print('Time to run: ' + str(np_int_test_time))
print(' ')
print('Size of Numpy String matrix: ' + str(sys.getsizeof(xs_np)))
print('Time to run: ' + str(np_str_test_time))
print(' ')
print('Size of Reg Digit matrix:  ' + str(sys.getsizeof(xd_reg)))
print('Time to run: ' + str(reg_int_test_time))
print(' ')
print('Size of Reg String matrix: ' + str(sys.getsizeof(xs_reg)))
print('Time to run: ' + str(reg_str_test_time))
print(' ')
print('Time to run: ' + str(if_else_version_time))
print(' ')
print('Time to run: ' + str(dict_version_time))
print(' ')