'''
Input is [1,2,3,4,5]
Output is 10 14
Explanation:
For the above sample input, 
1. If we sum all the values except 1, we get 14
2. If we sum everything except 2, we get 13
3. If we sum everything except 3, we get 12
4. If we sum everything except 4, we get 11
5. If we sum everything except 5, we get 10
So, the minimum sum is 10 and the maximum sum is 14. 
'''

def min_sum(input_list):
    '''
    returns minimum sum in the list
    '''
    x = input_list
    x.sort()
    n = len(x)
    s = 0
    for i in range(n):
        s =  s + x[i]
    min_ = s - x[n-1]

    return min_

def max_sum(input_list):
    '''
    returns maximum sum in the list
    '''
    x = input_list
    x.sort()
    n = len(x)
    s = 0
    for i in range(n):
        s =  s + x[i]
    max_ = s - x[0]

    return max_

def main():
    input_list = eval(input())
    print(min_sum(input_list), max_sum(input_list))

main()