'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

number of times bob occurs is: 2'''

def main():
    '''
@author : gvnaakhilsurya
Write a program that prints the number of times
 the sub string in the main string.
'''
    s = input()
n = len(s)
i = 0
C = 0
for i in range(0, n-2):
    if(s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b'):
        C = C+1
print(C)

if __name__== "__main__":
    main()
