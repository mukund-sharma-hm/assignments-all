"""Generating_List_of_Processes"""

import csv
import psutil

import decorator

@decorator.logger
def process_and_write_info():
    """processes and info"""
    dic = {}
    processes = psutil.process_iter()
    for process in processes:
        if process.name() in dic:
            dic[process.name()] += 1
        else:
            dic[process.name()] = 1
        print(process)

    for name, count in dic.items():
        print(f"{name}: {count}")

    with open("C:/js/python/Assignment/Processes.csv", 'w', encoding='utf-8', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Count'])

        writer.writerow({'Name': 'Process Name', 'Count': "Count"})
        for name, count in dic.items():
            writer.writerow({'Name': name, 'Count': count})

process_and_write_info()
