# Application Handling

This Python script contains functions to handle various tasks related to application monitoring, input validation, logging, Fibonacci series generation, processing and writing process information to a CSV file, reversing a string, generating squares of even numbers, and finding the top three most frequent characters in a string.

## Tasks Overview

### Application Monitoring
- Description: The `monitor_app` function monitors the specified application process and terminates it if the number of instances exceeds the specified limit.
- Code Location: `Application_handling.py`
- Usage: Execute the script to monitor the application process and manage instances.
- Dependencies: `psutil`

### Argument Validation Decorator
- Description: The `validate_args` decorator validates user input arguments and raises a `ValueError` if the input is not within the specified range.
- Code Location: `Application_handling.py`
- Usage: Apply the decorator to functions that require argument validation.

### Logging Decorator
- Description: The `logger` decorator logs details of function calls, including the module name, function name, execution date and time, arguments passed, and execution time.
- Code Location: `Application_handling.py`
- Usage: Apply the decorator to functions to enable logging.

### Fibonacci Series Generation
- Description: The `fibonacci` function generates a Fibonacci series up to the specified number.
- Code Location: `Application_handling.py`
- Usage: Execute the script to input a number and generate the Fibonacci series.

### Process Information Processing and Writing to CSV
- Description: The `process_and_write_info` function processes and counts running processes, then writes the information to a CSV file.
- Code Location: `Application_handling.py`
- Usage: Execute the script to process and write process information to a CSV file.
- Dependencies: `csv`

### String Reversal
- Description: The `reverse_string` function reverses a given string.
- Code Location: `Application_handling.py`
- Usage: Execute the script to input a string and print its reversed form.

### Square of Even Numbers
- Description: The `sq_even_numbers` function generates squares of all even numbers in the given range, with input validation using the `validate_args` decorator.
- Code Location: `Application_handling.py`
- Usage: Execute the script to input a number and print the squares of even numbers in the range.

### Top Three Most Frequent Characters
- Description: The `top_three_characters` function finds the top three most frequent characters in a given string.
- Code Location: `Application_handling.py`
- Usage: Execute the script to input a string and print the top three most frequent characters.
- Dependencies: `decorator`

## Additional Information
- Make sure to install the required dependencies (`psutil`, `decorator`, `csv`) before executing the scripts.
- For tasks involving input validation, ensure that the input is within the specified range.
- Feel free to modify the scripts or use them as reference for similar tasks.

