# Write a python program to find the square root of the given number
# using approximation method
#@author:gvnaakhilsurya
# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    s = input()
    # epsilon and step are initialized
    # don't change these values
    
    EPSILON = 0.01
    STEP = 0.1
    SQUARE = int(input())
    GUESS = 0.0
    while GUESS <= SQUARE:
        if abs(GUESS**2-SQUARE) < EPSILON:
            break
        else:
            GUESS += STEP
print(str(GUESS))
if __name__== "__main__":
    main()
