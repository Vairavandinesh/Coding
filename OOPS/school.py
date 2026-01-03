#Write a Python program to create a class called "School" with attributes for students, 
# teachers, and classes, and methods to add and remove students and teachers, 
# and to create classes.
#attributes - students,teachers,classes
#methods - addstudent,removestudent,addteacher,removeteacher,create class
class School:
    students=[]
    teachers=[]
    classes=[]
    def addStudent(self,name):
        School.students.append(name)
    def removeStudent(self,name):
        if name not in School.students:
            return
        School.students.pop(name)
    def addTeacher(self,teacherName):
        School.teachers.append(teacherName)
    def removeTeacher(self,teacherName):
        if teacherName not in School.teachers:
            return
        School.teachers.pop(teacherName)
    def createClass(self,subject):
        if subject in School.classes:
            return
        School.classes.append(subject)
    @classmethod
    def printer(cls):
        print(cls.students)
        print(cls.teachers)
        print(cls.classes)
obj1=School()
obj1.addStudent('ajith')
obj1.createClass('racing')
obj1.addTeacher('kumar')
School.printer()

