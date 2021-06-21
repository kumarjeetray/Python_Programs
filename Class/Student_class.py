class Student:
    def __init__(self, name, stream, roll_no, cgpa, lives_in_hostel):
        self.name = name
        self.stream = stream
        self.roll_no = roll_no
        self.cgpa = cgpa
        self.lives_in_hostel = lives_in_hostel

name_s = input("Enter Name:")
stream_s = input("Enter Stream:")
roll_no_s = eval(input("Enter Roll Number:"))
cgpa_s = eval(input("Enter Cgpa:"))
lives_in_hostel = input("Enter True if you love in hostel else False:")
student1 = Student(name_s, stream_s, roll_no_s, cgpa_s, lives_in_hostel)
print("Name:",student1.name)
print("Stream:",student1.stream)
print("Cgpa:",student1.cgpa)
print("Lives in hostel:",student1.lives_in_hostel)
