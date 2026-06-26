#file handling
#read logicdocument.doc
#file = open("logicdocument.doc", "r")
#content = file.read()
#print(content)
#file.close()

#Lab Exercise 1: write file with content "I love python programming"
"I am becoming a data scientist"
 
file = open("myfile.txt", "w")
file.write("I love python programming\n")
file.write("I am becoming a data scientist\n")
print("File written successfully.")
file.close()

#appending a file
file = open("myfile.txt", "a")
file.write("I am learning file handling in python\n")
print("File appended successfully.")
file.close()
