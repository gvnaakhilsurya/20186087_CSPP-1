''' Write a python program to find the square root of the given number
# using approximation method
#@author:gvnaakhilsurya
# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991'''

def main():
    ''' the square root of the given number'''
    eplison = 0.01
    step = 0.1
    square = int(input())
    guess = 0.0
    while guess <= square:
        if abs(guess**2-square) < eplison:
            break
        else:
            guess += step
    print(str(guess))
if __name__ == "__main__":
    main()
