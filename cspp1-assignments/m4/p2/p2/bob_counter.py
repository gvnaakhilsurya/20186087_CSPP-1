'''Assume s is a string of lower case characters.
Write a program that prints the number
 of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl',
 then your program should print
number of times bob occurs is: 2'''

def main():
    '''
@author : gvnaakhilsurya
Write a program that prints the number of times
 the sub string in the main string.
'''
str_input = input()
NUM_LEN = len(str_input)
i = 0
c = 0
for i in range(0, NUM_LEN-2):
    if(str_input[i] == 'b' and str_input[i+1] == 'o' and str_input[i+2] == 'b'):
        c = c+1
print(c)

if __name__ == "__main__":
    main()
