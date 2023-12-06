# Importar modulos
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Funciones
def leer_csv():
    with open('employees.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [row for row in csv_reader]

def get_employee_names():
    employees = leer_csv()
    print([employee['name'] for employee in employees])

def get_department_salaries():
    employees = leer_csv()
    department_salaries = {}
    for employee in employees:
        department = employee['department']
        salary = float(employee['salary'])
        if department not in department_salaries:
            department_salaries[department] = 0
        department_salaries[department] += salary
    print(department_salaries)

def get_highest_paid_employee():
    employees = leer_csv()
    highest_paid_employee = max(employees, key=lambda x: float(x['salary']))
    print(highest_paid_employee['name'])