

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float) and 0.0 > float(gpa) > 4.0:
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def display(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

if __name__ == '__main__':
    student1 = Student('Doe', 'Jane', 'Basketweaving', 2.3)
    print(student1.display())
    student2 = Student('Piper', 'Peter', 'Agronomy', 1.2)
    print(student2.display())