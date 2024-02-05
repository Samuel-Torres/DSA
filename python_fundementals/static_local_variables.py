class Student:
    """Version 1.0: creates a new instance of a student class""" # this is doc string which gets printed in the '__str__' method.

    college = "UCLA" # static variable. 

    def __init__(self, name, roll, grade): # this is the initialization constructor method which runs on initialization.
        self.name = name # object variables
        self.roll = roll
        self.grade = grade
        # can assign static variables here as well.
        print(f"A new student named {name} has been added to the roster.")

    def __str__(self):
        return "This is a Student class."

    def display(self): # class method
        print("Student name: ", self.name)
        print("Student roll: ", self.roll)
        print("Student grade: ", self.grade)
        print("Student college: ", Student.college)


new_student = Student("Sam", 100, 98.2)
new_student.display()