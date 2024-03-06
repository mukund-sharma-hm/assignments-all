"""decorator to check ia user input valid arguments"""

def validate_args(func):
    """function to validate arguments passed """

    def wrapper(num):
        if num < 1 or num > 10:
            raise ValueError("Number should be in range of 1 to 10")
        return func(num)
    return wrapper

