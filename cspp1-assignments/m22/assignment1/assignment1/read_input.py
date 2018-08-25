'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    lines = int(input())
    list_ = []
    for i in range(lines):
        list_.append(input())
    for i in list_:
        print(i)

if __name__ == '__main__':
    main()
