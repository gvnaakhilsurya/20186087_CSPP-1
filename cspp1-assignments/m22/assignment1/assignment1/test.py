

def print_dictionary(dictionary):
    """print dictionary"""
    # pass
    keys = sorted(dictionary.keys())
    for key in keys:
        print(key, "-", dictionary[key])

def main():
    """this is main"""
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
print_dictionary.py
Displaying print_dictionary.py.