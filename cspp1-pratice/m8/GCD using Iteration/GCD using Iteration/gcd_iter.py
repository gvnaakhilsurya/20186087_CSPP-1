# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a==0 or b==0:
        return 0
    elif a==1:
        return 1
    elif b==1:
        return 1
    else:
        max_i=max(a,b)
        res=0
        for i in range(1,max_i):
            if a%i==0 and b%i==0:
                res=i
        return(res)

    

def main():
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__== "__main__":
    main()