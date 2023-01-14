def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

class_standings = class_standing_generator()
for cls in class_standings:
  print(cls)

def class_standing_generator1():
    result = []
    result.append('Freshman')
    result.append('Sophomore')
    result.append('Junior')
    result.append('Senior')

    return result

print('-'*35)
print(class_standing_generator1())


def generator():
  i = 0
  while True:
    try:
      yield i
    except GeneratorExit:
      print("Early exit, BYE!")
      break
    i += 1
 
my_generator = generator()
for item in my_generator:
  print(item)
  if item == 1:
    my_generator.close()


# Generator Pipleines
def course_generator():
    yield ("Computer Science", 5)
    yield ('Art', 10)
    yield ('Business', 15)

def add_five_students(courses):
  for course in courses:
    yield (course[0], course[1] + 5)


increased_courses = add_five_students(course_generator())
for l in increased_courses:
  print(l)
print('*' * 50)

def summa():
    yield 'Summa Cum Laude'
def magna():
    yield 'Magna Cum Laude' 
def cum_laude():
    yield 'Cum Laude'
# Write your code below:

#generator function
def graduation_countdown(days):
  while days >= 0:
    days_left = yield days
    if days_left is not None:
      days = days_left
    else:
      days-=1

days = 25

#generator expression
countdown_generator = (i for i in range(days, -1, -1))

grad_days = graduation_countdown(days)
for day in grad_days:
  print(f'Days Left : {day}')
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  # print("Days Left: " + str(day))
  print(f'Days Left : {day}')

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()

print('-' *35)
gpas = [3.2, 4.0, 3.6, 2.9]

honors = honors_generator(gpas)
for h in honors:
  print(h)