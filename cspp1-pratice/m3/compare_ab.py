'''
@author : gvnaakhilsurya
Write a piece of Python code that ssume that two variables, varA and varB,
are assigned values,
either numbers or strings.
Write a piece of Python code that
evaluates varA and varB,
and then prints out one of the following messages:
"string involved"
if either varA or varB are strings
"bigger"
if varA is larger than varB
"equal"
if varA is equal to varB
"smaller"
if varA is smaller than varB
'''
VARA = 30
VARB = 20
if isinstance(VARA, str) or isinstance(VARB, str) == str:
    print("string involved")
if  VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
