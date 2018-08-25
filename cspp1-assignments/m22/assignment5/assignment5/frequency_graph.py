'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	'''
	'''
	if dictionary[word] not in dictionary:
        dictionary[word] = dictionary[word].strip()
	if dictionary[word] in dictionary:
		dictionary[word] = '#'
	else:
		dictionary[word] += '#'
	return dictionary

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
