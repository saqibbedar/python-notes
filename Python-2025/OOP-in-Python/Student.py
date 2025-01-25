# In python "__" prefix is used to make member variables and methods as private
# __init__ is a constructor function in python
# self refers to the first object, and is equivalent to this in C++
# super() is used to call a method from a parent class. It is commonly used for inheritance to make sure that parents class constructor __init__ is called, and allows child class to inherit and extend functionality of the parent class. 
# Super is same like we do in C++, we have to call the constructor of parent class before we set the constructor of child class so that we can inherit all the attributes form parent properly
# We call super for methods too, to inherit them if we want, as we have done for display method in Graduate class.


class Student:
    def __init__(self, id, name, semester, subjects):
        self.__id = id
        self.__name = name
        self.__semester = semester
        self.__subjects = subjects

    # Private methods (Abstraction)
    def __is_pass(self):
        for subject, marks in self.__subjects.items():
            if marks < 50:
                return False
        return True
    
    def __avg(self):
        total_marks = sum(self.__subjects.values()) # sum of total_marks
        total_subjects = len(self.__subjects) # total no. of subjects
        return total_marks/total_subjects

    # Public method
    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_semester(self, semester):
        self.__semester = semester

    def get_semester(self):
        return self.__semester
    
    def set_subjects(self, subjects):
        self.__subjects = subjects
    
    def set_subjects(self):
        return self.__subjects

    def update_student(self, id=None, name=None, semester=None, subjects=None):
        if id is not None:
            self.__id = id
        if name is not None:
            self.__name = name
        if semester is not None:
            self.__semester = semester
        if subjects is not None:
            self.__subjects = subjects

    def display(self):
        print("ID: ", self.__id, "\nName: ", self.__name)
        if self.__semester is not None:
            print("Semester: ", self.__semester)
        print("Subjects Marks: ", self.__subjects)
        print("Average: ", self.__avg())
        print("Status: ", "Pass" if self.__is_pass() else "Fail")

# Inheritence
class GraduateStudent(Student):
    def __init__(self, id, name, year_of_graduation, subjects, thesis_title):
        super().__init__(id, name, None, subjects) # pass None for semester
        self.__year_of_graduation = year_of_graduation
        self.__thesis_title = thesis_title
    
    # Polymorphism
    def display(self):
        super().display() 
        print("Year of Graduation: ", self.__year_of_graduation)
        print("Thesis Title: ", self.__thesis_title)

