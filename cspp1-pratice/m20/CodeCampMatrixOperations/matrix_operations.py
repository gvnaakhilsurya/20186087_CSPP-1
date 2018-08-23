def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    matrix_add = []
    rows = len(m1)
    coloums = len(m1[0])
    matrix_add = re_mat(rows,coloums)
    for i in range(rows):
        for j in range(coloums):
            matrix_add[i][j]= matrix_1[i][j]+matrix_2[i][j]
    return matrix_add


def re_mat(rows,coloums):
    add_matrix = [[0]*coloums]*rows
    return add_matrix

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    list_input = input().split(',')
    rows,coloums = int(list_input[0]),int(list_input[1])
    for _ in range(rows):
        list_matrix_row = input().split()
        if coloums == len(list_matrix_row):
            matrix.append([int(i) for i in list_matrix_row])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():

    # read matrix 
    matrix_1 = read_matrix ()
    # read matrix 2
    matrix_2 = read_matrix ()
    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
