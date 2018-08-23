'''
program that return True whether the given string has
more number of vowels than consonants, otherwise return False.
'''
def count_vowels(string_input):
    '''
    returns number of vowels in the given string parameter.
    '''
    cnt1 = 0
    for char in string_input:
        if char in 'aeiou':
            cnt1 += 1
    return cnt1

def count_consonants(string_input):
    '''
    returns number of consonants in the given string parameter.
    '''
    cnt2 = 0
    for char in string_input:
        if char not in 'aeiou':
            cnt2 += 1
    return cnt2
def is_vowels_count_higher(string_input):
    '''
    returns true if vowels count is greater than consonants count, otherwise false
    '''
    if count_vowels(string_input) > count_consonants(string_input):
        return True
    return False

def main():
    string_input = input()
    print(is_vowels_count_higher(string_input))

main()