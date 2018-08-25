'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    dictionary = {}
    user_string = string.replace(',.:;""','').split()
    for word in user_string:
        if word not in dictionary:
            word = word.strip()
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary
            
def main():
    string = ' '
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string +='\n'
    print(tokenize(string))


if __name__ == '__main__':
    main()
