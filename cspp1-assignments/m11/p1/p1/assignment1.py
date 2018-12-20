'''
Exercise: Assignment-1
The first step is to implement some code that
allows us to calculate the score for a single word.
The function get_word_score should accept as input a string
of lowercase letters (a word) and return the integer
score for that word, using the game's scoring rules.
'''
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
def get_word_score(word, n_num):
    sum_points = 0
    for i in word:
        if i in SCRABBLE_LETTER_VALUES:
            sum_points += SCRABBLE_LETTER_VALUES[i]
    sum_points = sum_points * len(word)
    if len(word) == n_num:#n_num is the length of scrabble letters given by user,
    #if we can arrange a valid word at a time then we will add +50 to it.
        sum_points = sum_points + 50
    return sum_points
def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
