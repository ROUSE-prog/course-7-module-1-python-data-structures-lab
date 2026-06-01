# This module contains operations related to sets.


# Creates a set of unique student majors
def unique_majors(students):
    return {student[2] for student in students}