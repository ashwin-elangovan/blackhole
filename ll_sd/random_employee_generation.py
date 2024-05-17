import random
from datetime import datetime, timedelta

class Employee:
    def __init__(self, name, date_of_joining, salary, address):
        self.name = name
        self.date_of_joining = date_of_joining
        self.salary = salary
        self.address = address

    def __repr__(self):
        return f"Employee(name={self.name}, DOJ={self.date_of_joining}, Salary={self.salary}, Address={self.address})"

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def generate_random_employee(self, num_employees):
        for _ in range(num_employees):
            name = self.generate_random_name()
            date_of_joining = self.generate_random_date_of_joining()
            salary = random.randint(30000, 100000)  # Random salary between $30,000 and $100,000
            address = self.generate_random_address()
            employee = Employee(name, date_of_joining, salary, address)
            self.employees.append(employee)

    def generate_random_name(self):
        first_names = ['John', 'Emma', 'Michael', 'Olivia', 'William', 'Sophia', 'James', 'Ava', 'Alexander', 'Mia']
        last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
        return random.choice(first_names) + ' ' + random.choice(last_names)

    def generate_random_date_of_joining(self):
        start_date = datetime(2010, 1, 1)
        end_date = datetime.now()
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        return random_date.strftime('%Y-%m-%d')

    def generate_random_address(self):
        zipcodes = ['10001', '10002', '10003', '10004', '10005']  # Sample zipcodes
        return {
            'street': f'{random.randint(1, 100)} Main Street',
            'city': 'New York',
            'state': 'NY',
            'zipcode': random.choice(zipcodes)
        }

    def search_employees(self, zipcode=None, min_salary=None, max_salary=None):
        filtered_employees = []
        for employee in self.employees:
            if zipcode and employee.address['zipcode'] != zipcode:
                continue
            if min_salary and employee.salary < min_salary:
                continue
            if max_salary and employee.salary > max_salary:
                continue
            filtered_employees.append(employee)
        return filtered_employees

# Example usage:
employee_manager = EmployeeManager()
employee_manager.generate_random_employee(50)

# Search for employees in a specific zipcode
employees_in_zipcode = employee_manager.search_employees(zipcode='10001')
print("Employees in zipcode 10001:")
for employee in employees_in_zipcode:
    print(employee)

# Search for employees with salary between $40,000 and $60,000
employees_in_salary_range = employee_manager.search_employees(min_salary=40000, max_salary=60000)
print("\nEmployees with salary between $40,000 and $60,000:")
for employee in employees_in_salary_range:
    print(employee)
