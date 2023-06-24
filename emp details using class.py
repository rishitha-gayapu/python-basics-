class Employee:
    def __init__(self):
        self.emp_id=int(input("emp id="))
        self.emp_name=input("emp_name=")
        self.emp_salary=int(input("emo_sal="))
        self.emp_dept=input("emp_dept=")
    def calculate_emp_salary(self,emp_salary,hours_worked):
        if(hours_worked>50):
            overtime=hours_worked-50
            overtime_amount=(overtime*(emp_salary/50))
            self.emp_salary+=overtime_amount
            print(self.emp_salary)
        else:
            print(self.emp_salary)
    def print_employee_details(self):
        print("emp_id=",self.emp_id)
        print("emp_name=",self.emp_name)
        print("emp_salary=",self.emp_salary)
        print("emp_dept=",self.emp_dept)
obj=Employee()
obj.calculate_emp_salary(300000,80)
obj.print_employee_details()
            
        
