def sum_of_digits(x):
	'''
	integer parameter x.
	return the sum of all the digits of given number
	'''
	sum_of_digits = 0
	while x >0:
		a_i = x % 10
		sum_of_digits = sum_of_digits + a_i
		x = x//10
	return sum_of_digits 

def main():
	x = int(input())
	print(sum_of_digits(x))

main()