#! python3 
# pyClassex.py

class Employee: 
	num_of_emps = 0 
	raise_amt = 1.04
	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.pay = pay
		self.email = first +'.'+last+'@company.com'
		Employee.num_of_emps+=1
		
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)
		
		
class Developer(Employee):
	raise_amt = 1.10
	
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, employees = None):
		super().__init__(first,last,pay)
		if employees is None: 
			self.employees = []
		else: 
			self.employees = employees
			
	def add_emp(self, emp): 
		if emp not in self.employees: 
			self.employees.append(emp)
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	def print_emps(self):
		for emp in self.employees:
			print('--->', emp.fullname())
	
dev_1 = Developer('Corey','Romero',50000, 'Python')
dev_2 = Developer('Test','User', 60000, 'Java')

mgr_1 = Manager ('Sue', 'Smith', 90000, [dev_1])


#isinstance() - shows if the class is part of the class, used: .isinstance(dev_1, Development/Employee) returns true .isinstane(dev_1,Manager) returns false

#issubclass - shows if the subclass (ex. Manager) is part of a class (Employee). Ex - issubclass(Manager, Employee) is true but issubclass(Manager, Developer) would be false as Manager is not a subclass of Developer