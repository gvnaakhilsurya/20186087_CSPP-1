
def check_duplicates(line):
    count = 0
    if "." not  in line:
        for i in line:
            count = line.count(i)
            if(count <= 9):
                print("Given sudoku is solved")
                break

def length_verify(line):
    if(len(line)== 81):
        check_duplicates(line)
    else:
        if(len(line)< 81):
            print("Invalid input")

def main():
    line = input()
    length_verify(line)
    # check_duplicates(line)
if __name__ == '__main__':
    main()