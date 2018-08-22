def same_last_digit(x, y):
	'''
	return True, if last digit in both the numbers are equal
	otherwise return False
	'''
	num_x = str(x)
	num_y = str(y)
	a_x = len(num_x)
	b_x = len(num_y)
	if num_x[a_x-1] == num_y[b_x-1]:
		return True
	return False

def main():
	x = int(input())
	y = int(input())
	print(same_last_digit(x,y))

main()