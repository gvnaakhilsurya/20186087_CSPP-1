'''
#@author:akhilsurya
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
# number and returns the factorial of given number.
# This function takes in one number and returns one number.
'''
def factorial_num(var_n):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if var_n == 0 or var_n == 1:
        return 1
    else:
         return var_n * factorial_num(var_n-1)

def main():
    '''
    main function

    '''
    var_n = input()
    print(factorial_num(int(var_n)))    
if __name__ == "__main__":
    main()
