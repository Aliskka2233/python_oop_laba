class User:
  name = None
  def show(self):
    print(self.name)
user = User()
user.name = 'Alise' 
user.show()

class Employee:
  name = None
  def salar(self):
    print(self.name)
    print(self.salary)
employee = Employee()
employee.name = 'Clara'
employee.salary = '275$'
employee.salar()