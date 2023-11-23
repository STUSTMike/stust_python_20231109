class Employee:
    def __init__(self,name,id,salary,department):
        self.id=id
        self.name=name
        self.salary=salary
        self.department=department
    #change the department of an employee
    def assign_departmemt(self,x):
        self.department=x

#######################################################
    #print the details of an employee
    def print_employee_details(self):
        print("ID:{} NANE:{} SALAY:{} DEPARTMENT:{}".format(self.id,self.name,self.salary,self.department))
    #Calculate overtime pay

######################################################
    def calculate_emp_salary(self,hour):
        if(hour>50):
            hours_worked=hour-50
            Overtime=(hours_worked * (self.salary/50))
            print("Overtime amount is:{}".format(Overtime))
        else:
            print("NO Overtime amount ")

#########################################################
text=Employee("ADAMS","E7876",50000,"ACCOUNTING")

text.print_employee_details()
text.assign_departmemt("OPERATIONS")
text.print_employee_details()
text.calculate_emp_salary(0)

# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"