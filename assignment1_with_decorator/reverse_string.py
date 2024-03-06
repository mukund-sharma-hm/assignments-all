"""reverse_string"""

import decorator

@decorator.logger
def reverse_string(string):
    """fucntion to reverse a string"""

    word_list = string.split()

    stack = []

    for word in word_list:
        stack.append(word)

    reversed_words = []


    while stack:
        reversed_words.append(stack.pop())


    reversed_string = " ".join(reversed_words)

    return reversed_string


input_string = input("Enter the string you want to reverse: -> ")

REVERSED = reverse_string(input_string)
print("Reversed string:", REVERSED)
