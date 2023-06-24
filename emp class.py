class Employee:
    def __init__(self):
        self.emp_id=input("enter emp id")
        self.emp_name=input("enter emp name")
        self.emp_salary=int(input("enter emp salary"))
        self.emp_department=input("enter emp dep")
    def calculate_emp_salary(self,hours_worked):
        if hours_worked>50:
            overtime=hours_worked-50
            overtime_amount=(overtime*(self.emp_salary//50))
            self.emp_salary+=overtime_amount
            print(self.emp_salary)
        else:
            print(self.emp_salary)
    def print_employee_details(self):
        print("employee id=",self.emp_id)
        print("employee name=",self.emp_name)
        print("emp salary =",self.emp_salary)
        print("emp dep =",self.emp_department)
obj1=Employee()
obj1.calculate_emp_salary(60)
obj1.print_employee_details()

