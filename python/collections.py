from collections import OrderedDict

import collections

orders = OrderedDict({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99},
          'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
 
orders.move_to_end('order_4829')
orders.popitem()
print(orders)

print(dir(collections.OrderedDict))


'''Deque'''

from collections import deque

import csv

def process_csv_supplies():
    data = []
    with open('python\supplies_data.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            data.append(row)
    return data

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!
supplies_deque = deque()

for item in csv_data:
  if item[2] =='important':
    supplies_deque.appendleft(item)
  else:
    supplies_deque.append(item)

print(supplies_deque)
print()

ordered_important_supplies = deque()
num = 25
while num:
  item = supplies_deque.popleft()
  ordered_important_supplies.append(item)
  num-=1
print(ordered_important_supplies)
print()


# namedtuples
clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

# Write your code below!
from collections import namedtuple

ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)
coat_cost = new_coat.price
print(coat_cost)
print()

updated_clothes_data = []
for cloth in clothes:
  updated_clothes_data.append(ClothingItem(cloth[0], cloth[1], cloth[2], cloth[3]))

print(updated_clothes_data)

ordered_unimportant_supplies = deque()
num = 10
while num:
  item = supplies_deque.pop()
  ordered_unimportant_supplies.append(item)
  num-=1
print(ordered_unimportant_supplies)


# defaultdict
from collections import defaultdict
site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
validated_locations = defaultdict(lambda : 'TODO: Add to website')
validated_locations.update(site_locations)
print(validated_locations)
print()
for item in updated_products:
  print(item)
  site_locations[item] = validated_locations[item]

print()
print(site_locations)


# OrderedDict

from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

# Write your code below!
orders = OrderedDict(order_data)
to_move = []
to_remove = []

for i, (k,v) in enumerate(orders.items()):
  # print(k)
  # print(i, k, v)
  if v == 'returned':
    to_move.append(k)
  if v == 'canceled':
    to_remove.append(k)


for item in to_remove:
  if item in orders:
    orders.pop(item)


for item in to_move:
  orders.move_to_end(item)
print(orders)
print()
    


# ChainMap
from collections import ChainMap
year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!
profit_map = ChainMap(*year_profit_data)
print(profit_map)
print()

def get_profits(chainmap):
  holiday = 'holiday'
  standard_profit, holiday_profit = 0, 0
  for key, value in chainmap.items():
    if holiday in key:
      holiday_profit += value
    else:
      standard_profit += value
  return standard_profit, holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

print()

for item in new_months_data:
  # print(item)
  profit_map = profit_map.new_child(item)

print()
print(profit_map)

print()

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
print(year_diff_standard_profit)

year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit
print(year_diff_holiday_profit)


# Counter
from collections import Counter
opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# Write your code below!
print(dir(Counter))
print()

def find_amount_sold(opening, closing, item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)

  opening_count.subtract(closing_count)
  print(opening_count.most_common())
  
  
  return opening_count[item]

print()
tshirts_sold = find_amount_sold(opening_inventory, closing_inventory, 't-shirt')


print(tshirts_sold)


# UserDict
from collections import UserDict

data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

# Write your code below!
class OrderProcessingDict(UserDict):
  def clean_orders(self):
    keys_to_del = []
    for key, value in self.data.items():
      print(key, '-' ,value)
      if value['order_status'] == 'complete':
         keys_to_del.append(key)
    
    for keys in keys_to_del:
      del self.data[keys]




process_dict = OrderProcessingDict(data)
process_dict.clean_orders()

print()
print(process_dict)

# UserList
from collections import UserList
data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
class ListSorter(UserList):
  def append(self, value):
    self.data.append(value)
    self.data.sort()

sorted_list = ListSorter(data)
sorted_list.append(2)
print(sorted_list)

# UserString
from collections import UserString

str_name = 'python powered patterned products'
str_word = 'patterned '


# print(dir(UserString))
print()
# Write your code below!
class SubtractString(UserString):
  def __sub__(self, other):
    if other in self.data:
      self.data = self.data.replace(other, '')

subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)


'''
deque
An advanced container which is optimized for appending and popping items from the front and back. 
For accessing many elements positioned elsewhere, it is better to use a list.

namedtuple
The namedtuple lets us create an immutable data structure similar to a tuple, but we don’t have 
to access the stored data using indices. Instead, we can create instances of our namedtuple with 
named attributes. We can then use the . operator to retrieve data by the attribute names.

Counter
This advanced container automatically counts the data within a hashable object which we pass into 
it’s constructor. It stores it as a dictionary where the keys are the elements and the values are 
the number of occurrences.

defaultdict
An advanced container which behaves like a regular dictionary, except that it does not throw an 
error when trying to access a key which does not exist. Instead, it creates a new key:value pair
where the value defaults to what we provide in the constructor for the defaultdict.

OrderedDict
The OrderedDict combines the functionality of a list and a dict by preserving the order of elements, 
but also allowing us to access values using keys without having to provide an index for the position 
of stored dictionaries.

ChainMap
This interesting container combines multiple mappings into a single container. When accessing a value 
using a key, it will search through every mapping contained within until a match is found or the end 
is reached. It also provides some useful methods for grouping parent and child mappings.

UserDict
This is a container wrapper which lets us create our own version of a dictionary

UserList
This is a container wrapper which lets us create our own version of a list

UserString
This is a container wrapper which lets us create our own version of a string
'''