class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        return(f"{self.name} is studying hard.")

    def check_grade(self, score):
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        return f"{self.name}'s grade is {grade}"
    
class InternationalStudent(Student):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country
    def study(self):
        return f"{self.name} is studying hard in {self.country}."
    def take_exam(self):
        return f"{self.name} is taking an exam in {self.country}."

print("======================================================")

student01 = Student("a",12)
grade = student01.check_grade(95)

print(f"{student01.name} is {student01.age} years old.")
print(student01.study())
print(grade)

print("======================================================")

student02 = InternationalStudent("b", 13, "Sweden")

print(f"{student02.name} is {student02.age} years old.")
print(student02.study())
print(student02.take_exam())

print("======================================================")