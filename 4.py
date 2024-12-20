class Employee:
     age = None
     name = None
     salary = None
employee = Employee()
employee2 = Employee()

employee.age = 66
employee.name = 'Clara'
employee.salary = 55

employee2.age = 22
employee2.name = 'Alise'
employee2.salary = 87

print(employee.age)
print(employee.name)
print(employee.salary)

print(employee2.age)
print(employee2.name)
print(employee2.salary)