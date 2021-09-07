# Create an hierarchy of classes - abstract class Employee and subclasses
# HourlyEmployee, SalariedEmployee, Manager and Executive. Every one's pay
# is calculated differently, research a bit about it. After you've established
# an employee hierarchy, create a Company class that allows you to manage the
# employees. You should be able to hire, fire and raise employees.

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first + "." + self.last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


class HourlyEmployee(Employee):
    def __init__(self, first, last, wage, num_hours, raise_rate=1.1):
        super().__init__(first, last)
        self.wage = wage
        self.num_hours = num_hours
        self.raise_rate = 1.1 if raise_rate is None else raise_rate

    def calc_pay(self):
        pay = float(self.wage * self.num_hours)
        return pay


class SalariedEmployee(Employee):
    def __init__(self, first, last, salary, num_period=12, raise_rate=1.15):
        super().__init__(first, last)
        self.salary = salary
        self.num_period = 12 if num_period is None else num_period
        self.raise_rate = 1.15 if raise_rate is None else raise_rate

    def calc_pay(self):
        pay = float(self.salary // self.num_period)
        return pay


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


class Company:
    company_income = 1000000

    def __init__(self, company_name, initial_employees=[]):
        self.name = company_name
        self.employees = initial_employees

    def hire_hourly_employee(self, first, last, wage, num_hours, raise_rate):
        employee = HourlyEmployee(first, last, wage, num_hours, raise_rate)
        self.employees.append(employee)

    def hire_salaried_employee(self, first, last, salary, num_period, raise_rate):
        employee = SalariedEmployee(first, last, salary, num_period, raise_rate)
        self.employees.append(employee)

    def hire_manager(self, first, last, base, extra_rate, raise_rate):
        employee = Manager(first, last, base, extra_rate, raise_rate)
        self.employees.append(employee)

    def hire_executive(self, first, last, base, extra_rate, bonus_rate, raise_rate):
        employee = Executive(first, last, base, extra_rate, bonus_rate, raise_rate)
        self.employees.append(employee)

    def fire_emp(self):
        pass

    def give_raise(self):
        pass

    def view_emps(self):
        pass

    def update_income(self):
        pass

    def get_details(self):
        pass


def example_januszex():
    family = [Executive('Jan', 'Kowalski', 10000), SalariedEmployee('Katarzyna', 'Kamyk', 50000, 12)]

    hourly_employees = [{'first': 'John', 'last': 'White', 'wage': 15, 'hours': 240},
                        {'first': 'Alice', 'last': 'Fox', 'wage': 20, 'hours': 200}]
    salaried_employees = [{'first': 'Alice', 'last': 'Sam', 'salary': 40000},
                          {'first': 'Maya', 'last': 'Wypok', 'salary': 42000, 'raise': 1.2}]
    managers = [{'first': 'Kylie', 'last': 'Smith', 'base': 5000},
                {'first': 'Samson', 'last': 'Kowalsky', 'base': 6000, 'extra': 0.15, 'raise': 1.22}]
    executives = [{'first': 'Ping', 'last': 'Zen', 'base': 8500}]

    januszex = Company(company_name='janusz-ex', initial_employees=family)

    for employee in hourly_employees:
        first = employee['first']
        last = employee['last']
        wage = employee['wage']
        hours = employee['hours']
        raise_rate = employee['raise'] if 'raise' in employee.keys() else None
        januszex.hire_hourly_employee(first, last, wage, hours, raise_rate)

    for employee in salaried_employees:
        first = employee['first']
        last = employee['last']
        salary = employee['salary']
        periods = employee['periods'] if 'periods' in employee.keys() else None
        raise_rate = employee['raise'] if 'raise' in employee.keys() else None
        januszex.hire_salaried_employee(first, last, salary, periods, raise_rate)

    for employee in managers:
        first = employee['first']
        last = employee['last']
        base = employee['base']
        extra = employee['extra'] if 'extra' in employee.keys() else None
        raise_rate = employee['raise'] if 'raise' in employee.keys() else None
        januszex.hire_manager(first, last, base, extra, raise_rate)

    for employee in executives:
        first = employee['first']
        last = employee['last']
        base = employee['base']
        extra = employee['extra'] if 'extra' in employee.keys() else None
        bonus = employee['bonus'] if 'bonus' in employee.keys() else None
        raise_rate = employee['raise'] if 'raise' in employee.keys() else None
        januszex.hire_executive(first, last, base, extra, bonus, raise_rate)

    return januszex


def main():
    example_januszex()


if __name__ == '__main__':
    main()
