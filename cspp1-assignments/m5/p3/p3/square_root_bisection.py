'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991
'''

def main():
	'''
	# epsilon and step are initialized
	# don't change these values
	'''
	X_NUM = int(input())
	EPSILON = 0.01
	LOWER = 0.0
	HIGHER = X_NUM
	BI_VAL = (HIGHER + LOWER)/2.0
	while abs(BI_VAL**2 - X_NUM) > EPSILON:
	    if BI_VAL**2 < X_NUM:
	        LOWER = BI_VAL
	    else:
	        HIGHER = BI_VAL
	    BI_VAL = (HIGHER + LOWER)/2.0
	print(BI_VAL)


if __name__== "__main__":
	main()
