class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def capitalize_first_letter(self, string):
        if string:
            return string[0].upper() + string[1:]
        return string

    def initials(self):
        Name = self.capitalize_first_letter(self.name)
        Surname = self.capitalize_first_letter(self.surname)
        return f"{Name[0]}.{Surname[0]}."

student = Student("Clara", "Nous")
print(student.initials())