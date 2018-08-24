def is_validation(n):
    tic1_list = n
    if tic1_list.count('x') > 5 or  tic1_list.count('o') > 5 :
        return "invalid game"
    for i in range(len(tic1_list)):
        for j in tic1_list[0]:
            if j not in 'ox.':
                return "invalid input"
    return 1


def main():
    x = ['x', 'x', 'x', 'x', 'o', 'x', 'x', 'x', 'x']
    print(is_validation(x))

       
main()