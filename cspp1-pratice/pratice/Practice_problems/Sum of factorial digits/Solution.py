def fact(n):
	'''
	Use this function fact(n), which takes n as integer and returns n!
	'''
	if n in (0,1):
		return 1
	else:
		return n*fact(n-1)
def sum_of_fact(n):
	'''
	argument : n, integer type.
	return type: integer, which is the sum of factorial of each digit in n.
	example : 123 = 1! + 2! + 3! = 1 + 2 + 6 = 9
	Your task is to write code here and use fact(n) to find factorial for each digit.
	'''
	if n > 0:
		sum_of_fact = 0
		while n>0:
			sum_of_fact =sum_of_fact + fact(n%10)
			n = n//10
		return sum_of_fact
	else:
		return 1


def main():
	print(sum_of_fact(int(input())))

main()