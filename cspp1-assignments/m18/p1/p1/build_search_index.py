'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

import re
def load_stopwords(filename):
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(string):
    regex = re.compile('[^a-z]')
    return [regex.sub("", w.strip()) for w in string.lower().split(" ")]
def build_search_index(docs):
    dict_1 = {}
    STOP_WORD = load_stopwords("stopwords.txt")
    for index, line in enumerate(docs):
        LIST_ = remove_stopwords(word_list(line), STOP_WORD)
        for ele in set(LIST_):
            if ele in dict_1:
                dict_1[ele].append((index, LIST_.count(ele)))
            else:
                dict_1[ele] = [(index, LIST_.count(ele))]
    return dict_1

def remove_stopwords(word, STOP_WORD):
    LIST_1 = word
    for w_1 in word:
        if w_1 in STOP_WORD:
            LIST_1.remove(w_1)
    return LIST_1
def print_search_index(index):

    keys = sorted(index.keys())
    for key in keys:
    print(key, " - ", index[key])
def main():
    '''
        main function
    '''
    documents = []
    lines = int(input())
    for i in range(lines):
        documents.append(input())
        i += 1

    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
