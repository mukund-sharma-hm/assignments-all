# Assignment

This Python script contains multiple tasks, each performing different operations.

## Tasks Overview

### Task 1: Consecutive Days
- Description: This task generates a list of tuples containing consecutive days from the given tuple.
- Code Location: `Consecutive_days.py`
- Usage: Execute the script to generate and print the list of consecutive days.

### Task 2: Day Details Dictionary
- Description: This task creates a dictionary with detailed information about each day, including its position, abbreviation, lowercase and uppercase forms, and length.
- Code Location: `Day_details.py`
- Usage: Execute the script to print the dictionary containing day details.

### Task 3: Character Occurrence in Days
- Description: This task creates a tuple with the occurrence of each character in each day's name.
- Code Location: `Character_occurrence.py`
- Usage: Execute the script to print the tuple with character occurrences.

### Task 4: Excel Operations
- Description: This task involves various operations on Excel files, such as generating fake employee data, retrieving data from Excel, performing calculations, and updating records.
- Code Location: `Excel_operations.py`
- Dependencies:
  - `openpyxl`: Required for reading and writing Excel files.
  - `faker`: Required for generating fake employee data.
  - `tabulate`: Required for formatting data into tables.
- Usage: Execute the respective functions to perform the desired operation.
  - `fake_employee_data()`: Generate fake employee data and save it to an Excel file.
  - `get_emp_with_max_salary()`: Retrieve the employee with the topmost salary.
  - `business_unit_with_highest_aggregated_salary()`: Retrieve the business unit with the highest aggregated salary.
  - `employee_with_highest_salary_per_bu()`: Retrieve the employee with the highest salary in each business unit.
  - `delete_employee_with_least_salary()`: Delete the record of the employee with the least salary.
  - `update_employee_salary(emp_id, new_salary)`: Update the salary details of an employee.

## Additional Information
- Make sure to install the required dependencies before executing the scripts.
- For tasks involving Excel operations, ensure that the Excel file paths are correctly specified.
- Feel free to modify the scripts or use them as reference for similar tasks.

