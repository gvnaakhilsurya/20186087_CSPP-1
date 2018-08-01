'''
@author : gvnaakhilsurya
Write a piece of Python code that prints out a for loop
that sum of the values 1 through end,
inclusive.end is a variable that
we define
foryou.
So,forexample,
if we define end to be 6,
your code should print out the result:
21
which is 1 + 2 + 3 + 4 + 5 + 6.
'''
END = int(input("Enter the end int value :"))
SUM = 0
for i in range(1, END+1, 1):
    SUM += i
print(SUM)
