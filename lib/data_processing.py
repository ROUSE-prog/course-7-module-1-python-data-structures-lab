# This module contains functions to process student data.


# Formats a single student's data into a readable string
def format_student_data(student):
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


# Loops through all students and prints formatted student data
def display_students(students):
    for student in students:
        print(format_student_data(student))