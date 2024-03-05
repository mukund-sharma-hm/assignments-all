"""aggragate employee by similar business units"""
import json


def aggregate_employee_data(input_file, output_file):
    """func to create aggragated data base on BU's"""
    with open(input_file, 'r', encoding='uts-8') as f:
        employee_data = json.load(f)

    aggregated_data = {}

    for employee in employee_data:
        business_unit = employee["Business Unit"]
        if business_unit not in aggregated_data:
            aggregated_data[business_unit] = []
        aggregated_data[business_unit].append(employee)

    with open(output_file, 'w', encoding='uts-8') as f:
        json.dump(aggregated_data, f, indent=4)

if __name__ == "__main__":
    INPUT = "task 4 and 5\\Employee_Personal_Details.json"
    OUTPUT = "task 4 and 5\\Aggregated_Employee_Data.json"
    aggregate_employee_data(INPUT, OUTPUT)
    print(f"Aggregated employee data saved to {OUTPUT}")
