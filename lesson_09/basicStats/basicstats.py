# For this project, you will `import` the **statistics** module.
# Write a class called Student that has two **private** data members - the student's name and grade.  
# It should have an init method that takes two values and uses them to initialize the data members. It should have a `get_grade` method.
# Write a separate function (not part of the Student class) called `basic_stats` 
# that takes as a parameter a list of Student objects and returns a tuple containing the mean, median, and mode of all the grades.  
# To do this, use the mean, median and mode functions in the [statistics module](https://docs.python.org/3/library/statistics.html). 
# Your `basic_stats` function should return those three values as a tuple, in the exact order given above.
# As an example, your code could be called as follows by the grader:

# s1 = Student("Kyoungmin", 73)
# s2 = Student("Mercedes", 74)
# s3 = Student("Avanika", 78)
# s4 = Student("Marta", 74)

# student_list = [s1, s2, s3, s4]
# print(basic_stats(student_list))  # should print a tuple of three values
"""
from statistics import mean, median, mode

class Student:
    def __init__(self,student_name,grade):
        self.student_name = student_name
        self.grade = grade

    def get_grade(self):
        return self.grade

def basic_stats(student_list): #returns a tuple containing the mean, median and mode of all grades
    grades = []
    for student in student_list:
        grades.append(student.get_grade())
        print(student_list)

    # mean(student_list)
    # median(student_list)
    # mode(student_list)

s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))  # should print a tuple of three values
"""

import statistics as s

class Student:
    def __init__(self,name,grade):
        self._name = name
        self._grade = grade
    
    def get_grade(self):
        return self._grade

def basic_stats(student_object_list):   #returns a tuple containing the mean,median, and mode of all grades
    all_grades = []         # [student.get_grade() for studet in student_object_list]
    mean = s.mean(all_grades)
    median = s.median(all_grades)
    mode = s.mode(all_grades)
    grade_tuple = (mean,median,mode)
    for student in student_object_list:
        all_grades.append(student.get_grade())
    return grade_tuple
    
s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
# print(basic_stats(student_list))  # should print a tuple of three values
print(basic_stats(student_list))