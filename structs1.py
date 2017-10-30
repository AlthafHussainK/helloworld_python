import csv
from student import Student 

students = []
for i in range(3):
    name = input("name: ")

    place = input("place: ")

    students.append(Student(name, place))

file = open("students.csv", "w")
writer = csv.writer(file)
for student in students:
    writer.writerow((student.name, student.place))
file.close()
    
