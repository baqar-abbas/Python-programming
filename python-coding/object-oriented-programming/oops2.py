class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Inheritance OOPS

class Student(Person):
    def __init__(self, name, age, roll_no, course ):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def show_student_details(self):
        self.show_details()
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")

class GraduateStudent(Student):
    def __init__(self, name, age, roll_no, course, thesis_topic):
        super().__init__(name, age, roll_no, course)
        self.thesis_topic = thesis_topic

    def show_graduate_details(self):
        self.show_student_details()
        print(f"Thesis Topic: {self.thesis_topic}")

student1 = GraduateStudent(
    "Aman",
    22,
    "CS101",
    "BSc Computer Science",
    "Machine Learning in Education"
)

student1.show_graduate_details()

student2 = Student(
    "Ravi",
    20,
    "CS102",
    "BSc Computer Science"
)
student2.show_student_details()