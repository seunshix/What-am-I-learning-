import itertools
from roster import student_roster

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def __iter__(self):
    self.count = 0
    return self
  
  def __next__(self):
    self.count +=1
    student = self.sorted_names[self.index]
    if self.count >= len(self.sorted_names):
      raise StopIteration
    return student

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students
  
  def get_student_seating(self):
    twos_seating = []
    twos_combos = itertools.combinations(self.sorted_names, 2)
    for combo in twos_combos:
      twos_seating.append(combo)
    return twos_seating


