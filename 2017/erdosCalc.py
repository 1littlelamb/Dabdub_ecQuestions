# Erdos Woods Finder

# Finding an erdos woods number is extremely compute intensive and as far as I can tell requires 
# a lot of trial and error. Other methods are hella complicated and I cbf!

from tqdm import tqdm

def primeFactorization(n):
	divisors = [ d for d in range(2,n//2+1) if n % d == 0 ]
	return [ d for d in divisors if \
			all( d % od != 0 for od in divisors if od != d ) ]

howMany = input('\n' + 'How many Erdos-Woods numbers would you like to find? ' + '\n' + '\n' +\
				'NOTICE: THIS ALGORITHM REQUIRES A LARGE AMOUNT OF COMPUTE POWER!' + '\n' + '\n' +\
				'Enter the number here: ')

erdos_nums = []

while len(erdos_nums) < int(howMany):
	for k in tqdm(range(24)):

		if k < 2:
			continue

		a_list = []
		min_extrema = 0
		max_extrema = 0
		primes_min = []
		primes_max = []
		primes_master = []

		for a in range(2400):
			if a <= k:
				continue

			a_list = [a+i for i in range(k+1)]

			primes_min = primeFactorization(a_list[0])
			primes_max = primeFactorization(a_list[-1])

			primes_master = (primes_max + primes_min)

			if all(any(elem in primes_master for elem in primeFactorization(i)) for i in a_list[1:-1]):
				print(f'Erdos-Woods found: k={k} a={a}')
				erdos_nums.append(k)
				break