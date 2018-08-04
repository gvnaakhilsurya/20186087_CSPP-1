'''
@author:gvnaakhilsurya
Given a  number int_input, find the product of all the digits
example: 
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    n = int(input())
    p = 1
    i = 1
    while i>0:
        a = i%10
        i = i//10
        p = p*a
    print(p)

if __name__ == "__main__":
    main()
