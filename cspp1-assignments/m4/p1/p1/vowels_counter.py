'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
@author :gvnaakhil
'''
def main():
    S = input()
    NUMVOWELS = 0
    for char in S:
        if char == 'a' or char == 'e' or char == 'i' \
           or char == 'o' or char == 'u':
            NUMVOWELS += 1
    print(NUMVOWELS)

if __name__ == "__main__":
    main()
