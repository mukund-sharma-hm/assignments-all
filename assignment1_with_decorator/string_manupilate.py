"""Frequent characters"""
import decorator

@decorator.logger
def top_three_characters(string):
    """give top three characters"""
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    sorted_characters = sorted(count.items(), key=lambda x: x[0])
    sorted_count = sorted(sorted_characters, key=lambda x: x[1], reverse=True)

    return sorted_count[:3]

input_string = input("Enter the String: ")
result = top_three_characters(input_string)
print("Top three most frequent characters:", result)
