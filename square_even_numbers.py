"""generate squares of all even numbers in given range"""

import decorator
import check_arguments

@check_arguments.validate_args
@decorator.logger
def sq_even_numbers(value):
    """even number square 1-10"""

    return [x**2 for x in range(1, value+1) if x % 2 == 0]

user_input = int(input("Enter a number between 1 to 10: --> "))

ans = sq_even_numbers(user_input)

print(ans)
