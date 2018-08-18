'''
    Document Distance - A detailed description is given in the PDF
'''
import re

def get_clean_string(words):
    clear_string = re.sub(r'\w\s+', " ", words).replace(',','').replace('\'','')
    list_words = clear_string.lower().split()
    return list_words


def create_dictionary(list_words,stop_words):
    dict_i = {}
    for i in  list_words:
        if i not in stop_words:
            if i not in dict_i:
                dict_i[i] = 1
            else:
                dict_i[i] += 1
    return dict_i
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    stop_words = load_stopwords("stopwords.txt")
    list_words_one = get_clean_string(dict1)
    list_words_two = get_clean_string(dict2)
    dict1_i = create_dictionary(list_words_one,stop_words)
    dict2_i = create_dictionary(list_words_two,stop_words)
    print(dict1_i)
    print(dict2_i)


    # num_i = 0
    # den_i = 0
    # den1_i= 0
    # den2_i= 0
    # ans_i = 0
    # for i in dict_i:
    #     num_i  += dict_i[i][0] * dict_i[i][1]
    #     den1_i += math.sqrt(dict_i[i][0]) **2
    #     den2_i += math.sqrt(dict_i[i][1]) **2
    #     den_i = den1_i + den2_i
    # return num_i/den_i

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = "rakesh, is a bage23rrvsgv89fb man"
    input2 = "Sai,g78485i4hijg ida is jun samaram"

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()