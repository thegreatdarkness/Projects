# Create an hierarchy of classes - abstract class Employee and subclasses
# HourlyEmployee, SalariedEmployee, Manager and Executive. Every one's pay
# is calculated differently, research a bit about it. After you've established
# an employee hierarchy, create a Company class that allows you to manage the
# employees. You should be able to hire, fire and raise employees.

import argparse
import pandas as pd


# Create base class Employee
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first + "." + self.last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


# Create subclass HourlyEmployee
class HourlyEmployee(Employee):
    def __init__(self, first, last, wage, num_hours, raise_rate=1.1):
        super().__init__(first, last)
        self.wage = wage
        self.num_hours = num_hours
        self.raise_rate = 1.1 if raise_rate is None else raise_rate

    def calc_pay(self):
        pay = float(self.wage * self.num_hours)
        return pay


# Create subclass SalariedEmployee
class SalariedEmployee(Employee):
    def __init__(self, first, last, salary, num_period=12, raise_rate=1.15):
        super().__init__(first, last)
        self.salary = salary
        self.num_period = 12 if num_period is None else num_period
        self.raise_rate = 1.15 if raise_rate is None else raise_rate

    def calc_pay(self):
        pay = float(self.salary // self.num_period)
        return pay


# Create subclass Manager
class Manager(Employee):
    def __init__(self, first, last, base, extra_rate=0.1, raise_rate=1.2):
        super().__init__(first, last)
        self.base = base
        self.extra_rate = 0.1 if extra_rate is None else extra_rate
        self.raise_rate = 1.2 if raise_rate is None else raise_rate

    def calc_extra(self):
        extra = float(self.base * self.extra_rate)
        return extra

    def calc_pay(self):
        pay = float(self.base + self.calc_extra())
        return pay


# Create subclass Executive
class Executive(Employee):
    def __init__(self, first, last, base, extra_rate=0.1, bonus_rate=0.01, raise_rate=1.25):
        super().__init__(first, last)
        self.base = base
        self.extra_rate = 0.1 if extra_rate is None else extra_rate
        self.bonus_rate = 0.01 if bonus_rate is None else bonus_rate
        self.raise_rate = 1.25 if raise_rate is None else raise_rate

    def calc_extra(self):
        extra = float(self.base * self.extra_rate)
        return extra

    def calc_bonus(self, company_income):
        bonus = float(self.bonus_rate * company_income)
        return bonus

    def calc_pay(self, company_income):
        pay = float(self.base + self.calc_extra() + self.calc_bonus(company_income))
        return pay


# Create class Company
class Company:
    # Set initial values: company_income, initial empty lists of employees
    company_income = 1000000
    data_files = ['hourly.csv', 'salaried.csv', 'managers.csv', 'executives.csv']
    hourly_employees = []
    salaried_employees = []
    managers = []
    executives = []

    # Initialize class by defining company name and initial empty list of employees
    def __init__(self, company_name):
        self.name = company_name
        self.employees = [self.hourly_employees, self.salaried_employees, self.managers, self.executives]

    # Load data about employees from .csv files and create class objects for each employee
    def load_data(self):

        # Loop through .csv files and create class objects...
        for file in self.data_files:
            with open(file, encoding='utf-8-sig') as f:
                # ...for hourly employees and append them to hourly_employees list
                if file == 'hourly.csv':
                    content = f.readlines()
                    for line in content[1:]:
                        item = line.rstrip('\n').split(',')
                        employee = HourlyEmployee(item[0], item[1], item[2], item[3], float(item[4]))
                        self.hourly_employees.append(employee)
                # ...for salaried employees and append them to salaried_employees list
                elif file == 'salaried.csv':
                    content = f.readlines()
                    for line in content[1:]:
                        item = line.rstrip('\n').split(',')
                        employee = SalariedEmployee(item[0], item[1], item[2], int(item[3]), float(item[4]))
                        self.salaried_employees.append(employee)
                # ...for managers and append them to managers list
                elif file == 'managers.csv':
                    content = f.readlines()
                    for line in content[1:]:
                        item = line.rstrip('\n').split(',')
                        employee = Manager(item[0], item[1], item[2], float(item[3]), float(item[4]))
                        self.managers.append(employee)
                # ...for executives and append them to executives list
                else:
                    content = f.readlines()
                    for line in content[1:]:
                        item = line.rstrip('\n').split(',')
                        employee = Executive(item[0], item[1], item[2], float(item[3]), float(item[4]), float(item[5]))
                        self.executives.append(employee)
            f.close()
        return self.hourly_employees, self.salaried_employees, self.managers, self.executives

    def hire_hourly_employee(self, first, last, wage, num_hours, raise_rate):
        employee = HourlyEmployee(first, last, wage, num_hours, raise_rate)
        self.hourly_employees.append(employee)

    def hire_salaried_employee(self, first, last, salary, num_period, raise_rate):
        employee = SalariedEmployee(first, last, salary, num_period, raise_rate)
        self.salaried_employees.append(employee)

    def hire_manager(self, first, last, base, extra_rate, raise_rate):
        employee = Manager(first, last, base, extra_rate, raise_rate)
        self.salaried_employees.append(employee)

    def hire_executive(self, first, last, base, extra_rate, bonus_rate, raise_rate):
        employee = Executive(first, last, base, extra_rate, bonus_rate, raise_rate)
        self.salaried_employees.append(employee)

    # Fire employee: delete class object and remove from lists
    def fire_employee(self, first, last):
        for lst in self.employees:
            for employee in lst:
                if employee.first == first:
                    if employee.last == last:
                        lst.remove(employee)
                        del employee
                    else:
                        continue
                else:
                    continue
        return self.employees

    def give_raise(self):
        pass

    # Print employees' names with distinction to employee subclass
    @staticmethod
    def print_employees_names():
        print("Hourly employees:")
        hourly = pd.read_csv('hourly.csv', encoding='utf-8-sig', usecols=['First name', 'Last name'])
        hourly.index += 1
        print(hourly)
        print("Salaried employees:")
        salaried = pd.read_csv('salaried.csv', encoding='utf-8-sig', usecols=['First name', 'Last name'])
        salaried.index += 1
        print(salaried)
        print("Managers:")
        managers = pd.read_csv('managers.csv', encoding='utf-8-sig', usecols=['First name', 'Last name'])
        managers.index += 1
        print(managers)
        print("Executives:")
        executives = pd.read_csv('executives.csv', encoding='utf-8-sig', usecols=['First name', 'Last name'])
        executives.index += 1
        print(executives)

    def update_income(self, new_income):
        pass

    def get_details(self):
        pass

    def save_exit(self):
        # Update employees and individual lists
        # pass lists into csv
        pass


# Example use case
def main():
    company = Company(company_name='Janusz-ex')
    company.load_data()

    parser = argparse.ArgumentParser()
    parser.add_argument('--hire_hourly', '-hh', help="Hire hourly employee", nargs=True)
    parser.add_argument('--hire_salaried', '-hs', help="Hire salaried employee", nargs=True)
    parser.add_argument('--hire_manager', '-hm', help="Hire manager", nargs=True)
    parser.add_argument('--hire_executive', '-he', help="Hire executive", nargs=True)
    parser.add_argument('--fire', '-f', help="Fire employee", nargs=True)
    parser.add_argument('--raise', '-r', help="Give raise to employee")
    parser.add_argument('--names', '-v', help="Print employees names' list")
    parser.add_argument('--update_income', '-ui', help="Update company income", type=float)
    parser.add_argument('--get_details', '-gd', help="Get details about employee")
    args = parser.parse_args()
    if args.hire_hourly:
        company.hire_hourly_employee(*args.hire_hourly)
    elif args.hire_salaried:
        company.hire_salaried_employee(*args.hire_salaried)
    elif args.hire_manager:
        company.hire_manager(*args.hire_manager)
    elif args.hire_executive:
        company.hire_executive(*args.hire_executive)
    elif args.fire:
        company.fire_employee(*args.fire)
    elif args.names:
        company.print_employees_names()
    elif args.update_income:
        company.update_income(args.update_income)
    elif args.get_details:
        company.get_details()

    return company


if __name__ == '__main__':
    main()
