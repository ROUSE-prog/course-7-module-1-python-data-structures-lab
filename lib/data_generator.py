# This module contains functions to lazily generate student data.

# Generates students one at a time based on major
def student_generator(students, major):
    return (student for student in students if student[2] == major)