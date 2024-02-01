# Classes:

class Student:
    """Version 1.0: creates a new instance of a student class""" # this is doc string which gets printed in the '__str__' method. 

    def __init__(self, name, roll, grade): # this is the initialization constructor method which runs on initialization.
        self.name = name
        self.roll = roll
        self.grade = grade
        print(f"A new student named {name} has been added to the roster.")

    def __str__(self):
        return "This is a Student class."

    def display(self): # class method
        print("Student name: ", self.name)
        print("Student roll: ", self.roll)
        print("Student grade: ", self.grade)


new_student = Student("Sam", 100, 98.2)
new_student2 = Student("Eli", 102, 68.2)
new_student3 = Student("Danny", 101, 78.2)

new_student.display()
new_student2.display()
new_student3.display()

print(new_student3.__doc__) # how to print doc string above.

# You can explicitly call the init method on a class like so:
Sam = Student("Sam", 100, 98.2) # implicitly called
Sam.__init__("Sam", 100, 98.2) # explicitly called
