n = 1234523456789



def factorial_user(n):
	if n in (0,1):
		return 1
	else:
		return n * factorial_user(n-1)

def break_number_to_digits(n):
	sum_user = 0
	while n > 0:
		sum_user = sum_user + factorial_user(n%10)
		n = n //10
	return sum_user

print(break_number_to_digits(n))