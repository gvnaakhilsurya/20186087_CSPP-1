
def main():
    # the input string is in s
    # remove pass and start your code here
    '''
    program to print longest sequence in a string
    '''
    input_str = input()
    temp_str = ""
    for i in range(len(input_str)-1):
        sub_str = input_str[i]
        while i+1 < len(input_str) and input_str[i] <= input_str[i+1]:
            i=i+1
            sub_str = sub_str + input_str[i]
        if len(sub_str)>len(temp_str):
            temp_str = sub_str
    print(temp_str)

if __name__ == "__main__":
    main()

