#attendance System
#live demo

#name = input('Enter Student: ')
#with open('attendance.txt', 'a') as file:
#    file.write(name)
 #   file.write('\n')

import csv
with open('student.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
#add ['regno', 'name', 'age', 'gender', 'course']
#to the students.csv, using a dictionary csv writer