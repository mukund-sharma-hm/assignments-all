"""to delete employee and create seperate json to store data and raise salary for finance"""
import json
from config import employee_json


def delete_employee(employee_id, employee_file, terminated_file):
    """Function to delete employee and save terminated employees' names"""

    with open(employee_file, 'r', encoding='utf-8') as f:
        employee_data = json.load(f)
    if employee_id not in [employee['EMP ID'] for employee in employee_data]:
        raise ValueError(f"Employee with ID {employee_id} does not exist.")

    terminated_employee = [employee['EMP NAME'] for employee in employee_data if employee['EMP ID'] == employee_id][0]

    with open(terminated_file, 'a', encoding='utf-8') as f:
        f.write(terminated_employee + '\n')
        employee_data = [employee for employee in employee_data if employee['EMP ID'] != employee_id]

    with open(employee_file, 'w', encoding='utf-8') as f:
        json.dump(employee_data, f, indent=4)


def apply_salary_hike(business_unit, hike_percentage, employee_file):
    """Function to apply salary hike based on business unit"""

    with open(employee_file, 'r', encoding='utf-8') as f:
        employee_data = json.load(f)

    for employee in employee_data:
        if employee['Business Unit'] == business_unit:
            current_salary = employee['Salary']
            new_salary = current_salary * (1 + hike_percentage / 100)
            employee['Salary'] = new_salary
    with open(employee_file, 'w', encoding='utf-8') as f:
        json.dump(employee_data, f, indent=4)


if __name__ == "__main__":

    try:
        delete_employee('d85a2486-aad1-41a1-bf96-94a54f56c3cc', employee_json, 'terminated_employees.json')
        print("Employee terminated successfully.")
    except ValueError as e:
        print(e)

    apply_salary_hike('Finance', 10, employee_json)
    print("Salary hiked")
