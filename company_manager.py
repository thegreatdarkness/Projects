# Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager
# and Executive. Every one's pay is calculated differently, research a bit about it. After you've established an
# employee hierarchy, create a Company class that allows you to manage the employees. You should be able to hire,
# fire and raise employees.

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = self.first + "." + self.last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


class HourlyEmployee(Employee):
    hourly_emps = {
        "Name": [],
        "Pay": [],
    }

    def __init__(self, first, last, wage, num_hours):
        super().__init__(first, last)
        self.wage = wage
        self.num_hours = num_hours

    def calc_pay(self):
        pay = float(self.wage * self.num_hours)
        return pay

    def show_lst(self):
        return HourlyEmployee.hourly_emps


class SalariedEmployee(Employee):
    salaried_emps = {
        "Name": [],
        "Pay": [],
    }

    def __init__(self, first, last, salary, num_period):
        super().__init__(first, last)
        self.salary = salary
        self.num_period = num_period

    def calc_pay(self):
        pay = float(self.salary // self.num_period)
        return pay

    def show_lst(self):
        return self.salaried_emps


class Manager(Employee):
    managers = {
        "Name": [],
        "Pay": [],
    }

    def __init__(self, first, last, base, extra):
        super().__init__(first, last)
        self.base = base
        self.extra = extra

    def calc_extra(self):
        extra = float(self.base * self.extra)
        return extra

    def calc_pay(self):
        pay = float(self.base + self.extra)
        return pay

    def show_lst(self):
        return self.managers


class Executive(Employee):
    executives = {
        "Name": [],
        "Pay": [],
    }

    def __init__(self, first, last, base, extra, bonus):
        super().__init__(first, last)
        self.base = base
        self.extra = extra
        self.bonus = bonus

    def calc_extra(self):
        extra = float(self.base * self.extra)
        return extra

    def calc_bonus(self):
        bonus = float(0.01 * Company.company_income)
        return bonus

    def calc_pay(self):
        pay = float(self.base + self.extra + self.bonus)
        return pay

    def show_lst(self):
        return Executive.executives


class Company:

    company_income = 1000000

    emps = {
        "Hourly": HourlyEmployee.hourly_emps,
        "Salaried": SalariedEmployee.salaried_emps,
        "Managers": Manager.managers,
        "Executives": Executive.executives
    }

    def __init__(self):
        action = int(input("Options: 1 - Hire, 2 - Fire, 3 - Give raise, 4 - View, 5 - Exit: "))
        if action == 1:
            self.hire_emp()
        elif action == 2:
            self.fire_emp()
        elif action == 3:
            self.give_raise()
        elif action == 4:
            print(Company.emps)
        while action == 5:
            break
        else:
            print("Option not valid.")

    def hire_emp(self):
        emp_class = input("Enter Employee class (H/S/M/E): ")
        if emp_class == 'H':
            HourlyEmployee.first = str(input("Enter first name: "))
            HourlyEmployee.last = str(input("Enter last name: "))
            HourlyEmployee.wage = int(input("Enter wage: "))
            HourlyEmployee.num_hours = int(input("Enter number of hours: "))
            emp = HourlyEmployee(HourlyEmployee.first, HourlyEmployee.last, HourlyEmployee.wage,
                                 HourlyEmployee.num_hours)
            fullname = HourlyEmployee.fullname(emp)
            pay = HourlyEmployee.calc_pay(emp)
            HourlyEmployee.hourly_emps["Name"].append(fullname)
            HourlyEmployee.hourly_emps["Pay"].append(pay)
        elif emp_class == 'S':
            SalariedEmployee.first = str(input("Enter first name: "))
            SalariedEmployee.last = str(input("Enter last name: "))
            SalariedEmployee.salary = int(input("Enter salary: "))
            SalariedEmployee.num_periods = int(input("Enter number of periods: "))
            emp = SalariedEmployee(SalariedEmployee.first, SalariedEmployee.last, SalariedEmployee.salary,
                                   SalariedEmployee.num_periods)
            fullname = SalariedEmployee.fullname(emp)
            pay = SalariedEmployee.calc_pay(emp)
            SalariedEmployee.salaried_emps["Name"].append(fullname)
            SalariedEmployee.salaried_emps["Pay"].append(pay)
        elif emp_class == 'M':
            Manager.first = str(input("Enter first name: "))
            Manager.last = str(input("Enter last name: "))
            Manager.base = int(input("Enter base: "))
            Manager.extra = float(input("Enter extra: "))
            emp = Manager(Manager.first, Manager.last, Manager.base, Manager.extra)
            fullname = Manager.fullname(emp)
            Manager.calc_extra(emp)
            pay = Manager.calc_pay(emp)
            Manager.managers["Name"].append(fullname)
            Manager.managers["Pay"].append(pay)
        elif emp_class == 'E':
            Executive.first = str(input("Enter first name: "))
            Executive.last = str(input("Enter last name: "))
            Executive.base = int(input("Enter base: "))
            Executive.extra = int(input("Enter extra: "))
            Executive.bonus = int(input("Enter bonus: "))
            emp = Executive(Executive.first, Executive.last, Executive.base, Executive.extra, Executive.bonus)
            fullname = Executive.fullname(emp)
            Executive.calc_extra(emp)
            Executive.calc_bonus(emp)
            pay = Executive.calc_pay(emp)
            Executive.executives["Name"].append(fullname)
            Executive.executives["Pay"].append(pay)
        else:
            print("Employee class not valid.")
        return self.emps

    def fire_emp(self):
        pass

    def give_raise(self):
        pass
