def check_duplicates(line):
	chars = ".0123456789"
	count = 0
	if "." not  in line:
		for i in line:
			count = line.count(i)
			if(count == 9):
				print("Given sudoku is solved")
			elif:
				print("duplicates")
	
def length_verify(line):
	count = 0
	if(len(line)== 81 & check_duplicates(line)):
		

def main():
	line = input()
	length_verify(line)
if __name__ == '__main__':
	main()