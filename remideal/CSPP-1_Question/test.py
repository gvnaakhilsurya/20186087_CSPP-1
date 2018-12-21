

def main():
	s = "2156473983689521747943816525862.74931142.593867973816425821739546......"
	# count = 0
	# if "." not  in s:
	# 	for i in s:
	# 		count = s.count(i)
	# 		if(count <= 9):
	# 			print("comp")
	# 			break
	# 		else:
	# 			print("dpuli")
	if(len(s)== 81):
		print("comp")
	else:
		if(len(s)<81):
			print("invalid")

		

if __name__ == '__main__':
	main()
