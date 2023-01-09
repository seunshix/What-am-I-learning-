from classroom_organizer import ClassroomOrganizer
from roster import student_roster

import itertools

# Create an iterator that lists and print out each student info using next()
iterator = iter(student_roster)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print('-' *30)

# Create an iterator protocol in ClassroomOrganizer to print out the next student on the roll call
organizer = ClassroomOrganizer()
for name in organizer.sorted_names:
  print(name)

print('-' * 30)

# Create a combination that can organize student seating chart
student_seating = organizer.get_student_seating()
print(student_seating)

print('-' * 30)

math_lovers = organizer.get_students_with_subject('Math')
science_lovers = organizer.get_students_with_subject('Science')

math_and_science_lovers = itertools.chain(math_lovers, science_lovers)

for student in math_and_science_lovers:
  print(student)