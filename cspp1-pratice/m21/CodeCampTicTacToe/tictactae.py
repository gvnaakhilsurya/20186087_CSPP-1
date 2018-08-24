def is_win_tic_tac(n):
    tac_1 = empty_tictac()
    if tac_1[0][0] == tac_1[1][1] ==tac_1[2][2]:
        return tac_1[0][0]
    elif tac_1[0][2] == tac_1[1][1] ==tac_1[2][0]:
        return tac_1[0][2]
    elif tac_1[0][0] == tac_1[1][0] ==tac_1[2][0]:
        return tac_1[0][0]
    elif tac_1[0][1] == tac_1[1][1] ==tac_1[2][1]:
        return tac_1[0][1]
    elif tac_1[0][2] == tac_1[1][2] ==tac_1[2][2]:
        return tac_1[0][2]
    elif tac_1[0][0] == tac_1[0][1] ==tac_1[0][2]:
        return tac_1[0][0]
    elif tac_1[1][0] == tac_1[1][1] ==tac_1[1][2]:
        return tac_1 [1][0]
    elif tac_1[2][0] == tac_1[2][1] ==tac_1[2][2]:
        return tac_1[2][0]
    else:
        return ("invalid input")

def is_validation(n):
    tic1_list = full_string(n)
    if tic1_list.count('x') > 5 or  tic1_list.count('o') > 5 or tic1_list.count('x')== tic1_list.count('o') :
        return "invalid game"
    for i in range(len(tic1_list)):
        for j in tic1_list:
            if j not in 'ox.':
                return "invalid input"
    return 1


def empty_tictac():
    # it converts the input into lists
    tic = []
    for i in range(3):
        list_temp = input().split()
        tic.append(list_temp)
    return tic

def full_string(tic):
    l = []
    for i in tic:
        l.extend(i)
    return l


def main():
    inp_tic = empty_tictac()
    clean_string = full_string(inp_tic)
    if is_validation(n) == 1:
        print(is_win_tic_tac(n))

if __name__ == '__main__':
    main()

