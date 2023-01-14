guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    var = yield name, age
    if var is not None:
      var = var.split(',')
      name, age = var[0], int(var[1])
      guests[name] = age
      yield name, age


print('Print out the first 10 guests on the list')
guest_list = read_guestlist('python\eventCoordinator\guest_list.txt')
for i in range(10):
  print(next(guest_list))

print('-'*30)
print('Use a generator method to add new guest')
print(guest_list.send('Jane,35'))
for guest in guest_list:
  print(guest)

print('-'*30)
print('Generator Expression to generate guest over age 21')

guest_can_drink = (name for name, age in guests.items() if age >= 21)

for guest in guest_can_drink:
  print(guest)

print('-'*30)
print('Use generator functions to assign meals to tables')

def table1():
  meal = 'Amala and Ewedu'
  table = 1
  for seat in range(1, 6):
    yield f'You will be sitting on seat {seat} at table {table} and your meal is {meal}. Please enjoy!'

def table2():
  meal = 'Jollof Rice'
  table = 2
  for seat in range(1, 6):
    yield f'You will be sitting on seat {seat} at table {table} and your meal is {meal}. Please enjoy!'

def table3():
  meal = 'Catfish Peppersoup'
  table = 3
  for seat in range(1, 6):
    yield f'You will be sitting on seat {seat} at table {table} and your meal is {meal}. Please enjoy!'

def tables():
  yield from table1()
  yield from table2()
  yield from table3()

table = tables()

print('-'*30)
print('Using connected generators, assign tables to guests')


def assign_table(guests, tables):
  names = list(guests.keys())
  for name in names:
    yield (name, next(tables))

assigning_tables = assign_table(guests, tables())
for item in assigning_tables:
  print(item)

  

