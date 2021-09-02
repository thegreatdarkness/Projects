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
    hourly_emps = [{'Name': 'John White', 'Pay': 1440.0}, ]

    def __init__(self, first, last, wage, num_hours):
        super().__init__(first, last)
        self.wage = wage
        self.num_hours = num_hours

    def calc_pay(self):
        pay = float(self.wage * self.num_hours)
        return pay


class SalariedEmployee(Employee):
    salaried_emps = [{'Name': 'Alice Sam', 'Pay': 2000.0}, ]

    def __init__(self, first, last, salary, num_period):
        super().__init__(first, last)
        self.salary = salary
        self.num_period = num_period

    def calc_pay(self):
        pay = float(self.salary // self.num_period)
        return pay


class Manager(Employee):
    managers = [{'Name': 'Kylie Smith', 'Pay': 5000}, ]
    extra = None

    def __init__(self, first, last, base):
        super().__init__(first, last)
        self.base = base

    def calc_extra(self):
        self.extra = float(self.base * 0.10)
        return self.extra

    def calc_pay(self):
        pay = float(self.base + self.extra)
        return pay


class Executive(Employee):
    executives = [{'Name': 'Ping Zen', 'Pay': 10000}, ]
    extra = None
    bonus = None

    def __init__(self, first, last, base):
        super().__init__(first, last)
        self.base = base

    def calc_extra(self):
        self.extra = float(self.base * 0.20)
        return self.extra

    def calc_bonus(self):
        self.bonus = float(0.01 * Company.company_income)
        return self.bonus

    def calc_pay(self):
        pay = float(self.base + self.extra + self.bonus)
        return pay


class Company:

    company_income = 1000000

    emps = None
    action = None

    def __init__(self):
        self.emps = {
                     "Hourly": HourlyEmployee.hourly_emps,
                     "Salaried": SalariedEmployee.salaried_emps,
                     "Managers": Manager.managers,
                     "Executives": Executive.executives
                    }

    def hire_emp(self):
        emp_class = input("Enter Employee class (H/S/M/E): ")
        if emp_class == 'H':
            HourlyEmployee.first = str(input("Enter first name: "))
            HourlyEmployee.last = str(input("Enter last name: "))
            HourlyEmployee.wage = int(input("Enter wage: "))
            HourlyEmployee.num_hours = int(input("Enter number of hours: "))
            emp = HourlyEmployee(HourlyEmployee.first, HourlyEmployee.last,
                                 HourlyEmployee.wage, HourlyEmployee.num_hours)
            fullname = HourlyEmployee.fullname(emp)
            pay = HourlyEmployee.calc_pay(emp)
            HourlyEmployee.hourly_emps.append({"Name": fullname, "Pay": pay})
            print(fullname, "was added as Hourly employee")
        elif emp_class == 'S':
            SalariedEmployee.first = str(input("Enter first name: "))
            SalariedEmployee.last = str(input("Enter last name: "))
            SalariedEmployee.salary = int(input("Enter salary: "))
            SalariedEmployee.num_periods = int(input("Enter number of periods: "))
            emp = SalariedEmployee(SalariedEmployee.first, SalariedEmployee.last,
                                   SalariedEmployee.salary, SalariedEmployee.num_periods)
            fullname = SalariedEmployee.fullname(emp)
            pay = SalariedEmployee.calc_pay(emp)
            SalariedEmployee.salaried_emps.append({"Name": fullname, "Pay": pay})
            print(fullname, "was added as Salaried employee")
        elif emp_class == 'M':
            Manager.first = str(input("Enter first name: "))
            Manager.last = str(input("Enter last name: "))
            Manager.base = int(input("Enter base: "))
            emp = Manager(Manager.first, Manager.last, Manager.base)
            fullname = Manager.fullname(emp)
            Manager.calc_extra(emp)
            pay = Manager.calc_pay(emp)
            Manager.managers.append({"Name": fullname, "Pay": pay})
            print(fullname, "was added as Manager")
        elif emp_class == 'E':
            Executive.first = input("Enter first name: ")
            Executive.last = input("Enter last name: ")
            Executive.base = input("Enter base: ")

            emp = Executive(str(Executive.first), str(Executive.last), int(Executive.base))
            fullname = Executive.fullname(emp)
            Executive.calc_extra(emp)
            Executive.calc_bonus(emp)
            pay = Executive.calc_pay(emp)
            Executive.executives.append({"Name": fullname, "Pay": pay})
            print(fullname, "was added as Executive")
        else:
            print("Employee class not valid.")
        return self.emps

    def fire_emp(self):
        emp = input("Employee name to remove:")
        if emp in self.emps:
            pass

    def give_raise(self):
        pass

    @staticmethod
    def view_emps():
        hourly = HourlyEmployee.hourly_emps
        hourly_lst = []
        for item in hourly:
            values = item.get("Name")
            hourly_lst.append(values)
        print("Hourly employees:", hourly_lst)

        salaried = SalariedEmployee.salaried_emps
        salaried_lst = []
        for item in salaried:
            values = item.get("Name")
            salaried_lst.append(values)
        print("Salaried employees:", salaried_lst)

        managers = Manager.managers
        managers_lst = []
        for item in managers:
            values = item.get("Name")
            managers_lst.append(values)
        print("Managers:", managers_lst)

        executives = Executive.executives
        executives_lst = []
        for item in executives:
            values = item.get("Name")
            executives_lst.append(values)
        print("Executives:", executives_lst)

    @staticmethod
    def update_income():
        company_income = int(input("Update company income: "))
        return company_income

    @staticmethod
    def get_details(fullname):
        while True:
            for dic in HourlyEmployee.hourly_emps:
                for atr in dic:
                if fullname in dic:




def manage(Company):
    while True:
        action = input("Options: 1 - Hire, 2 - Fire, 3 - Give raise, 4 - Update income, "
                       "5 - Employee list, 6 - Get details, 7 - Exit: ")
        if action == '1':
            Company.hire_emp()
        elif action == '2':
            Company.fire_emp()
        elif action == '3':
            Company.give_raise()
        elif action == '4':
            Company.update_income()
        elif action == '5':
            Company.view_emps()
        elif action == '7':
            break
        else:
            print("Option not valid.")


def main():
    manage(Company())


if __name__ == '__main__':
    main()
