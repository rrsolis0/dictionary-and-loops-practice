# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
# print(len(students))
# print(students[4]['Combo,Name'])
# print(students[4]['Email'][0])
# print(students[4]['Email'][1])
# print(students[4]['GL'])

# for loops allow us to
#iterate through the data
#and perform some function

#we are iterating through the data
#and printing the name and email of the students
#we are also printing a line of underscores to separate the students
#we are also printing a line of underscores to separate the students
# for student in students:
#     print(student['Combo,Name'])
#     print(student['MName'])
#     print(student['LName'])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print("_"*25)


# we are asking the user to input their name
# then we are checking if the name is in the data
# if the name is in the data we are printing the name and "this works"
# name = input("what is you name?") 
id = int(input("What is your ID? "))
for student in students:
    if id == student['CPSID']:
        print(student['CPSID'])
        print("this works")


# Let's try to print out the emails of the students:    
# 1. Print Student Details
for student in students: # Iterate through all of the students in the dictionary
    print("Name: "+ (student['FName'] ) + " " + (student['LName'])) # Print out the student's first and last name
    print("Email 1: " + (student['Email'][0])) # Prints the student's first email
    print("Email 2: " + (student['Email'][1])) # Prints the student's second email
    print('_'*25)

##############################################
    
# 2. Search for Students in a Specifi Homeroom
hr = input("What is your Homeroom? ") # Asks user to input the homeroom that they are looking for
found = False
for student in students: # Iterates through the students in the dictionary
    if hr == student['HR']: # If the homeroom number the user inputs is the same as one of the homerooms in the dictionary, the following will occur:
        print(student['Combo,Name']) # Prints the name of the student(s) in this format: Last name, First name
        print(student['Email'][0]) # Prints out the first email of the student(s)
        print(student['Email'][1]) # Prints out the second email of the student(s)
        found = True # Because found = False above, this will change found to True
if not found: # Changes the found in the line directly above this one to False
    print("No students found in this homeroom.") 

###################################################
    
# 3. Check if a Student is in a list
student_in_list = input("Input the first name of a student: ").lower() #asks the user to input a name and then makes it all lowercase rarglessregardless if the user had it capitalized
for student in students: #iterates through the date inside the variable studnets
    if student_in_list == student['FName'].lower(): #checks if the user input is is inside the variable student
        print(student['Combo,Name']) #displays Last name & First
        print(student['HR'])#displays homeroom

