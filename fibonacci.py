"""Fibonacci series"""
import decorator


@decorator.logger
def fibonacci(n):
    """fibonacci series upto the given number n"""

    num1 = 0
    num2 = 1

    while num1 <= n:
        print(num1, end=" ")

        curr_num = num1+num2
        num1 = num2
        num2 = curr_num

fibonacci(int(input("Enter a number: ")))
