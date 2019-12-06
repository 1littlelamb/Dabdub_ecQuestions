#Finding the phone number

import math
import numpy as np
from perrinCalc import p
from tqdm import tqdm

a = open('text_files/numbers.txt', 'r').read()

list_original = np.array([int(s) for s in a.split(' ')])

def approximation_scan(list_, perrin_numbers):
	
	i = 0
	tolerance = 0.00000000000001

	for num in range(len(list_)):
		current_number = list_[i]
		if int(math.log10(current_number)) < 5:
			continue
		for perrin_number in perrin_numbers:
			if (current_number > (perrin_number - (perrin_number*tolerance))) and (current_number < (perrin_number + (perrin_number*tolerance))):
				list_ = np.delete(list_, i)
				i+= -1
		i+=1

	return list_

def remove_perrin(list_):

	perrin_numbers = np.array([3,0,2,3])
	n = 4
	i = 0

	for pos in tqdm(range(len(list_))):
		current_number = list_[i]
		if current_number not in perrin_numbers:
			perrin_number = perrin_numbers[-1]
			while perrin_number < current_number:
				perrin_number = p(n)
				perrin_numbers = np.append(perrin_numbers, perrin_number)
				n+=1
		if current_number in perrin_numbers:
			list_ = np.delete(list_, i)
			i+= -1


		i+=1

	list_ = approximation_scan(list_, perrin_numbers)

	return list_



list_noperrin = remove_perrin(list_original)

print(list_noperrin)
