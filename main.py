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
# id = int(input("What is your ID? "))
# for student in students:
#     if id == student['CPSID']:
#         print(student['CPSID'])
#         print("this works")


# Let's try to print out the emails of the students:    
# 1. Print Student Details
# for student in students: # Iterate through all of the students in the dictionary
#     print("Name: "+ (student['FName'] ) + " " + (student['LName'])) # Print out the student's first and last name
#     print("Email 1: " + (student['Email'][0])) # Prints the student's first email
#     print("Email 2: " + (student['Email'][1])) # Prints the student's second email
#     print('_'*25)

##############################################
    
# 2. Search for Students in a Specifi Homeroom
# hr = input("What is your Homeroom? ") # Asks user to input the homeroom that they are looking for
# found = False
# for student in students: # Iterates through the students in the dictionary
#     if hr == student['HR']: # If the homeroom number the user inputs is the same as one of the homerooms in the dictionary, the following will occur:
#         print(student['Combo,Name']) # Prints the name of the student(s) in this format: Last name, First name
#         print(student['Email'][0]) # Prints out the first email of the student(s)
#         print(student['Email'][1]) # Prints out the second email of the student(s)
#         found = True # Because found = False above, this will change found to True
# if not found: # Changes the found in the line directly above this one to False
#     print("No students found in this homeroom.") 

###################################################
    
# 3. Check if a Student is in a list
# student_in_list = input("Input the first name of a student: ").lower() #asks the user to input a name and then makes it all lowercase rarglessregardless if the user had it capitalized
# for student in students: #iterates through the date inside the variable studnets
#     if student_in_list == student['FName'].lower(): #checks if the user input is is inside the variable student
#         print(student['Combo,Name']) #displays Last name & First
#         print(student['HR'])#displays homeroom






# Update the dataset in memory (e.g., modify student details)
# for student in students:
#     if student['CPSID'] == 10000014:  # Example CPSID to update
#         student['FName'] = 'Ruy'
#         student['LName'] = 'Sois'
#         student['GL'] = 11
#         student['HR'] = 'B220'


# for student in students:
#     if student['CPSID'] == 10000015:  # Replace with the condition to find the specific student
#         del student['MName']  # Deletes the 'MName' key-value pair
#         del student['GL']
#         del student['HR']
#         del student['Email'][0]
#         del student['LName']
#         del student['FName']
#         print(f"Updated student: {student}")
    

# Update a specific entry by index
students[2]['FName'] = 'NewName'  # Updates the first student's first name
students[2]['LName'] = 'NewLastName'
print(students[2])


# Example: Add a 'ContactNumber' field to each student
for student in students:
    if student ['CPSID'] == 10000042:
        student['ContactNumber'] = '778-988-0987'  # Assign a default or specific value



# Create a new student dictionary
new_student = {
    'CPSID': 987654,
    'Combo,Name': 'Doe, John',
    'FName': 'John',
    'LName': 'Doe',
    'MName': 'Paul',
    'HR': 'B220',
    'GL': 11,
    'Email': ['john.doe@example.com', 'j.doe@example.org']
}



# Add the new student to the list
students.append(new_student)


# Collecting input from the user for each field
cpsid = int(input("Enter CPSID: "))
combo_name = input("Enter Combo,Name (Last, First): ")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
middle_name = input("Enter Middle Name: ")
homeroom = input("Enter Homeroom (e.g., B220): ")
grade_level = int(input("Enter Grade Level: "))
primary_email = input("Enter Primary Email: ")
secondary_email = input("Enter Secondary Email: ")

# Create a new student dictionary using the input
new_student = {
    'CPSID': cpsid,
    'Combo,Name': combo_name,
    'FName': first_name,
    'LName': last_name,
    'MName': middle_name,
    'HR': homeroom,
    'GL': grade_level,
    'Email': [primary_email, secondary_email]
}

# Add the new student to the list
students.append(new_student)

# Print confirmation and the new student details
print("New student added:")
print(new_student)
#################################
for student in students:
    student['ContactNumber'] = 'N/A'
print(students)






# Overwrite the `student_data.py` file with the updated data
# Overwrite the student_data.py file with formatted data
with open('student_data.py', 'w') as f:
    f.write("students = [\n")
    for student in students:
        formatted_student = "    {\n"
        for key, value in student.items():
            formatted_student += f"        '{key}': {repr(value)},\n"
        formatted_student = formatted_student.rstrip(",\n") + "\n    },\n"  # Clean trailing commas and newline
        f.write(formatted_student)
    f.write("]\n")

print("student_data.py has been updated with the original formatting.")

