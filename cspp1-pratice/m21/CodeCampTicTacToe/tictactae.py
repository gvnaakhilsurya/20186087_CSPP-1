def is_win_tic_tac(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[0][2]
    elif matrix[0][0] == matrix[1][0] == matrix[2][0]:
        return matrix[0][0]
    elif matrix[0][1] == matrix[1][1] == matrix[2][1]:
        return matrix[0][1]
    elif matrix[0][2] == matrix[1][2] == matrix[2][2]:
        return matrix[0][2]
    elif matrix[0][0] == matrix[0][1] == matrix[0][2]:
        return matrix[0][0]
    elif matrix[1][0] == matrix[1][1] == matrix[1][2]:
        return matrix [1][0]
    elif matrix[2][0] == matrix[2][1] == matrix[2][2]:
        return matrix[2][0]
    else:
        return ("invalid input")

def is_validation(matrix):
    tic1_list = full_string(matrix)
    if tic1_list.count('x') > 5 or  tic1_list.count('o') > 5  or  tic1_list.count('x')== tic1_list.count('o') : 
        return "invalid game"
    for i in range(len(tic1_list)):
        for j in tic1_list:
            if j not in 'ox.':
                return "invalid input"
    return 1


def empty_tictac():
    # it converts the input into lists
    matrix = []
    for i in range(3):
        list_temp = input().split()
        matrix.append(list_temp)
    return matrix

def full_string(matrix):
    l = []
    for i in matrix:
        l.extend(i)
    return l


def main():
    inp_tic = empty_tictac()
    clean_string = full_string(inp_tic)
    output = is_validation(clean_string)
    if output == 1:
        print(is_win_tic_tac(inp_tic))
    else:
        print(output)


if __name__ == '__main__':
    main()

