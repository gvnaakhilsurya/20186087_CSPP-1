def same_first_digit(x, y):
    '''
    return True, if first digit in both the numbers are equal
    otherwise return False
    '''
    num_x = int(str(abs(x))[0])
    num_y = int(str(abs(y))[0])
    if num_x == num_y:
        return True
    return False


def main():
    x = int(input())
    y = int(input())
    print(same_first_digit(x,y))

main()