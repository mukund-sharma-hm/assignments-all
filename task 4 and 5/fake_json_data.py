from faker import Faker
import json
import random


fake = Faker()


def generate_employee_details(details):
    """creating fake employee details"""
    employee_data = []
    business_units = ["Finance", "HR", "Marketing", "IT", "Operations"]

    for _ in range(details):
        emp_id = fake.uuid4()
        emp_name = fake.name()
        emp_email = fake.email()
        business_unit = random.choice(business_units)
        salary = fake.random_number(digits=5)  
        
        employee_data.append({
            "EMP ID": emp_id,
            "EMP NAME": emp_name,
            "EMP EMAIL": emp_email,
            "Business Unit": business_unit,
            "Salary": salary
        })

    return employee_data


def save_to_json(data, file_name):
    """saving data and creating json file"""
    with open(file_name, 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


num_records = random.randint(50, 100)
employee_personal_details = generate_employee_details(num_records)

FILENAME = "Employee_Personal_Details.json"
save_to_json(employee_personal_details, FILENAME)

print(f"{num_records} employee personal details created inside:->{FILENAME}")
