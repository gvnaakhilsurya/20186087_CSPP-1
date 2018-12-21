

def main():
	s = "726493815315728946489651237852147693673985124941362758194836572567214389238579461"
	count = 0
	if "." not  in s:
		for i in s:
			count = s.count(i)
			if(count <= 9):
				print("comp")
				break
			else:
				print("dpuli")

		

if __name__ == '__main__':
	main()
