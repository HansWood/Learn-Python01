class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

students = [
    Student("A", 75, 41, 85, 95),
    Student("B", 175, 41, 85, 95),
    Student("C", 75, 141, 85, 95),
    Student("D", 75, 41, 185, 95),
    Student("E", 75, 41, 85, 195),
]

for student in students:
    print(student.to_string())
