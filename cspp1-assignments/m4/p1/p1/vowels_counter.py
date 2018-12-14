'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
if s = 'azcbobobegghakl', your program should print:
@author :gvnaakhilsurya
Number of vowels: 5
'''
def main():
    '''
    Assume s is a string of lower case characters.
    Write a program that counts up the number of vowels contained in the string s
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
    '''
    str_input = input()
    num_vowels = 0
    for char in str_input:
        if char in "aioeu":
            num_vowels += 1
    print(num_vowels)

if __name__ == "__main__":
    main()
