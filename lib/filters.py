# This module contains functions for filtering student data.

# Returns only students that match the selected major
def filter_students_by_major(students, major):
    return [student for student in students if student[2] == major]