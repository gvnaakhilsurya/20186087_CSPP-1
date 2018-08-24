def repeated_indexed_characters(string_input):
	'''
	Write a program to display each character in the given word in the following way:
	Input : abcdef
	Output: bccdddeeeefffff (a is at 0 index, b at 1 index, c at 2 index……….)
	return string with above model.
	'''
	opera_ = string_input
	temp_ = ''
	for i,j in enumerate(opera_):
		temp_ = temp_ + i * j
	return temp_

def main():
	string_input = input()
	print(repeated_indexed_characters(string_input))

main()