#attendance System
#live demo

#name = input('Enter Student: ')
#with open('attendance.txt', 'a') as file:
#    file.write(name)
 #   file.write('\n')

import os
import csv

script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, 'student.csv')

with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
#add ['regno', 'name', 'age', 'gender', 'course']
#to the students.csv, using a dictionary csv writer

with open(csv_path, 'a', newline='') as file:
    fieldnames = ['regno', 'name', 'age', 'gender', 'course']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({'regno': '24/U/08843/PS', 'name': 'Naluyange Emilly Shirley', 'age': '20', 'gender': 'Female', 'course': 'Software Engineering'})
    file.write('\n')
    