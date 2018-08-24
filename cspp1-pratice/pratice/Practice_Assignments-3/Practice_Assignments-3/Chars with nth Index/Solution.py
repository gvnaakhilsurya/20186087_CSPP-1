def chars_nth_index(s, n):
	'''
	returns every nth character in the string
	input : 4, M$itc1hL@pa$$w0rd
	output : c@$d
	'''
	user_ = n 
	for i,j in enumerate(user_):
		if i%4


def main():
	s = input()
	n = int(input())
	print(chars_nth_index(s,n))
main()