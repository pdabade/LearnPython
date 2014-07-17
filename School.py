class SchoolMember:
	'''Represents any school member.'''
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print '(Initialized SchoolMember: {})'.format(self.name)
		
	def tell(self):
		'''Tell my details.'''
		print 'Name: "{}" Age: "{}"'.format(self.name,self.age),
		#The trailing comma is used at the end of the print statement in the superclass’stell() method to print a line and allow the next print to continue on the same line.This is a trick to make print not print a \n (newline) symbol at the end of the printing.
		
class Teacher(SchoolMember):
	'''Represents a teacher.'''
	
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print '(Initialized Teacher: {})'.format(self.name)
		
	def tell(self):
		SchoolMember.tell(self)
		print 'Salary: "{}"'.format(self.salary)
		
class Student(SchoolMember):
	'''Represents a student.'''
	
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks = marks
		print '(Initialized Student: {})'.format(self.name)
		
	def tell(self):
		SchoolMember.tell(self)
		print 'Marks: "{}"'.format(self.marks)
		
t = Teacher('Mrs.Puttu',33,100)
s = Student('Kishto',1,100)

members = [t,s]

print

for member in members:
	member.tell() 
	
