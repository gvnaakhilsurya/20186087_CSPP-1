def check_duplicates(line):
	chars = ".0123456789"
	count = 0
	if "." not  in line:
		for i in line:
			count = line.count(i)
			if(count > 9):
				return False
	return True

def main():

	s = "215647398368952174794381652586274931142593867973816425821739146659428.13437165281"
	print(len(s))
	# for i in s:
	# 	if "." in s:
	# 		print("is their")
# for i in line:
# 		count = check_string.count(i)
# 		if count >9:
# 			print("duplicates are there")
# 		elif:


if __name__ == '__main__':
	main()