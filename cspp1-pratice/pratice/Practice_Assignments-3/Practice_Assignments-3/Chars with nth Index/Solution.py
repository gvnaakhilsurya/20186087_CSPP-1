def chars_nth_index(s, n):
	'''
	returns every nth character in the string
	input : 4, M$itc1hL@pa$$w0rd
	output : c@$d
	'''

	temp_ = ''
	for i,j in enumerate(s):
		if i % n == 0 and i > 0:
			temp_ = temp_ + j
	return temp_

	

def main():
	n = int(input())
	s = input()
	print(chars_nth_index(s,n))
main()