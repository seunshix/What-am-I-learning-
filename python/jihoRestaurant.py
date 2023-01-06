tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)

'''
Play around and have fun with our new knowledge of function arguments. 
Here is some additional functionality that Jiho might like:

1. The ability to remove a table’s guests when they leave the restaurant.
2. An adjustment to the calculate_price_per_person() function to access a 
tables 'total' and return the result.
3. The ability to add and remove order items for both food and drinks if there is ever a mistake.
4.The ability to queue reservations for later times for specific tables.
'''