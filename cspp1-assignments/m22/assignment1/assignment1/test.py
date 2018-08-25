string = 'lorem ipsum porem lorem ipsum porem'
dictionary = {}
user_string = string.split()
for word in user_string:
	if word not in dictionary:
		word = word.strip()
	if word not in dictionary:
			dictionary[word] = 1
	else:
			 dictionary[word] += 1


            

print(dictionary)