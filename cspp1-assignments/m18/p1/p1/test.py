# my_list = ['Computers makes as many mistakes in one second as three men working for thirty years straight.',
#  'Talk is cheap. Show me the code.', "That's the thing about people who think they hate computers. What they really hate is lousy programmer.",
#   "I'm not a great programmer; I'm just a good programmer with great habits.",
#    'Any fool can write code that computers can understand. Good programmers write code that humans can understand.',
#  "At forty, I was too old to work as a programmer myself anymore; writing code is a young person's job."]
# ''
# x = my_list.join(e for e in my_list if e.isalnum())
# print(x)





# >>> string = "Special $#! characters   spaces 888323"
# >>> ''.join(e for e in string if e.isalnum())
# 'Specialcharactersspaces888323'


# import re
# def clean_up_words():
#     '''
#     cleaning the given words
#     '''
#     my_list = [''.join(c for c in s if c not in punctuation) for s in list]

# from tokens import tokenize
# from collections import Counter
# s='Computers makes as many mistakes in one second as three men working for thirty years straight.'
# words = Counter((t.text.lower() for t in tokenize(s) if t.type == 'word'))


#  mylist = ['Mixed Case One', 'Mixed Case Two', 'Mixed Three']
# # for i in mylist:
# #     i.lower()
# #     print(i)

# x = [item.lower() for item in mylist]
# print(x)





def clean(word):
    return ''.join(letter for letter in word.lower() if 'a' <= letter <= 'z')


print(clean(['Mixed Case One', 'Mixed Case Two', 'Mixed Three']))
