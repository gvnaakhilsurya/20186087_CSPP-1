'''# Exercise: Assignment-2
@author:gvnaakhilsurya
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.
'''

def sumofdigits(var_n):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if var_n== 0:
        return 0
    else:
        return (var_n %10 + sumofdigits(var_n//10))
 
def main():
    '''
    main function

    '''
    var_n= input()
    print(sumofdigits(int(var_n)))  

if __name__ == "__main__":
    main()

