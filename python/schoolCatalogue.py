class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name
  
  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, value):
    self.numberOfStudents = value

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students.'

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def get_pickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parent_repr = super().__repr__()
    return f'{parent_repr} The pickup policy is {self.pickupPolicy}.'
  

class MiddleSchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'middle', numberOfStudents)
    self.pickupPolicy = pickupPolicy
  
  def get_pickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parent_repr = super().__repr__()
    return f'{parent_repr} The pickup policy is {self.pickupPolicy}.'

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    parent_repr = super().__repr__()
    return f'{parent_repr} The sports teams are {self.sportsTeams}.'


sfis = HighSchool('Strong Foundation International School','116', ['Tennis', 'Basketball'])
print(sfis)

sfis.get_name()
sfis.get_level()
sfis.get_numberOfStudents()
sfis.set_numberOfStudents(215)