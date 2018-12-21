def length_verify(line):
	count = 0
	if(len(line)== 81):
		print("Given sudoku is solved")

def main():
	line = input()
	print(len(line))
	length_verify(line)
if __name__ == '__main__':
	main()