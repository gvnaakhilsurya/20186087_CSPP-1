def get_factorial_digit_from_number(n):
    sum_ = 0
    while n>0:
        sum_ = sum_ + factorial(n % 10)
        n = n//10
    return sum_
def factorial(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n*factorial(n-1)
def main():
    n = int(input())
    print(get_factorial_digit_from_number(n))

main()