"""
Program: Employee.py
Author: Andy Volesky
Last date modified: 11/03/2021
The purpose of this program:

Write an employee class.

The class attributes are the following:
last_name: string
first_name: string
address: string
phone_number: string
salaried: boolean
start_date: datetime
salary: double

Methods:
display() returns a string that when printed will follow the below format:

Sasha Patel
123 Main Street
Urban, Iowa
Salaried employee: $40,000/year       # OR Hourly employee: $7.25/hour
Start date: 6-28-2019
Note this will have some logic statements to check for salaried or hourly to construct the return string.

"""

class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, addy, phnum, salrd, stdate, slry, hrly):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phnum
        self.salaried = salrd
        self.start_date = stdate
        self.salary = slry
        self.hourly = hrly

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def display(self):
        if self.salaried == True:
            return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n"+str(self.salary) + "\n"+str(self.start_date)
        else:
            return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n"+str(self.hourly) + "\n"+str(self.start_date)

# Driver
emp = Employee('Ruiz', 'Matthew', '123 Main St.\nCarroll, IA 50401', '5159991111', True, '6-20-22', '$40,000 per year', '$7.25 per hour')
print(emp.display())
emp2 = Employee('Davis', 'Karla', '4545 5th St.\nAmes, IA 51041', '5159991111', False, '12-25-21', '$40,000 per year', '$7.25 per hour')   # call the construtor, needs to have a first and last name in parameter
print(emp2.display())
del emp
del emp2