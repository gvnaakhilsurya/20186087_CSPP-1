'''# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
author@:gvnaakhilsurya
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube'''

def main():
    ''''# input is captured in s
    '''
    cube = int(input())
    guess = 1
    while (guess**3) < cube:
        guess += 1
    if int(guess**3) == cube:
        print(cube, "is a perfect cube")
    else:
        print(cube, "is not a perfect cube")

if __name__ == "__main__":
    main()
