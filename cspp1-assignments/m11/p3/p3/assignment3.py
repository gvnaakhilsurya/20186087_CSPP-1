# Assignment-3
'''
@author:gvnaakhilsurya
At this point, we have written code to generate a random hand and display
that hand to the user. We can also ask the user for a word
(Python's input) and score the word (using your getWordScore).
However, at this point we have not written any code to verify that
a word given by a player obeys the rules of the game.
A valid word is in the word list; and it is composed entirely of
letters from the current hand. Implement the isvalid_word function.
Testing: Make sure the test_isValidWord tests pass. In addition,
you will want to test your implementation by calling it multiple
times on the same hand - what should the correct behavior be?
Additionally, the empty string ('') is not a valid word
- if you code this function correctly, you shouldn't need
an additional check for this condition.
Fill in the code for isvalid_word in ps4a.py and be sure you've
passed the appropriate tests in test_ps4a.py before pasting your
function definition here.
'''
def isvalid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    num_count = 0
    if word in word_list:
        for i in word:
            if i in hand:
                num_count += 1
    return num_count == len(word)
def main():
    '''
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    '''
    word = input()
    n_num = int(input())
    adict = {}
    for data in range(n_num):
        data = input()
        l_length = data.split()
        adict[l_length[0]] = int(l_length[1])
    l2_list = input().split()
    print(isvalid_word(word, adict, l2_list))
if __name__ == "__main__":
    main()
