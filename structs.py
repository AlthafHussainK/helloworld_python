from student import Student 

students = []
for i in range(3):
    name = input("name: ")

    place = input("place: ")

    students.append(Student(name, place))

for student in students:
    print("{} is in {}".format(student.name, student.place))
    