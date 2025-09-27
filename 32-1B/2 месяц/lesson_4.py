
class Datadase:   
    def __init__(self):
        self.student = []
        self.teacher = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(sel,teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

    def __str__(self):
        return f"Student: {self.name} ({self.student_id} Age: {self.age})"
    
class Teacher(Person):
    def __init__(self, name, age, sutbject):
        super().__init__(name, age)
        self.sutbject = sutbject


    def enroll(self):
        self.sutbject.append(sutbject)
        sutbject.add_teacher(self)

    def __str__(self):
        return f"Teacher: {self.name} Sutbject: {}"