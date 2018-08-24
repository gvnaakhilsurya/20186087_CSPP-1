

def is_validation(n):
    tic1_list = full_string()
    if tic1_list.count('x') > 5 or  tic1_list.count('o') > 5 :
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
    print(full_string(inp_tic))

if __name__ == '__main__':
    main()

