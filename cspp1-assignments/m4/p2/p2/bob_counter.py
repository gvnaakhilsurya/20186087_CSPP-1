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
STR_INPUT = input()
NUM_LEN = len(STR_INPUT)
i = 0
C = 0
for i in range(0, NUM_LEN-2):
    if(STR_INPUT[i] == 'b' and STR_INPUT[i+1] == 'o' and STR_INPUT[i+2] == 'b'):
        C = C+1
print(C)

if __name__ == "__main__":
    main()
