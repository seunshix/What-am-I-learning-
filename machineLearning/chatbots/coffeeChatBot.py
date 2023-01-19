# Define your functions

stopWords = ['stop', 'Stop', 'cancel', 'Cancel', 'quit', 'Quit']

def coffee_bot():
  print('Welcome to the cafe!')

  order_drink = 'y'
  drinks = []
  while order_drink == 'y':
    size = get_size()
    drink_type = get_drink_type()

    drink = f'{size} {drink}'

    temp = temperature()
    print(f"Alright, that's a {size} {temp} {drink_type}!")

    while True:
        order_drink = input('Would you like to order another drink? (y/n) \n> ')
        if order_drink in ['y', 'n']:
            break

  print(" Okay, I have")
  for drink in drinks:
    print(f'- {drink}')

  extra_options()
  
  name = input('Can I get your name please? \n> ')
  print(f"Thanks {name}! Your drink will be ready shortly.")

def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte() 

def extra_options():
  res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')
  if res == 'a':
    print('Okay, no problem! We\'ll get you a plastic cup.')
  elif res == 'b':
    print('Great! We\'ll fill up your reusable cup.')
  else:
    print_message()
    return extra_options()
# Call coffee_bot()!

def temperature():
  res = input('Would you like your drink hot or cold? \n[a] Hot \n[b] Iced \n> ')
  if res == 'a':
    return 'hot'
  elif res == 'b':
    return 'iced'
  else:
    print_message()
    return temperature()

def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n> ')
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    print_message()

# def extra_drink():
#   res = input('Would you like another drink? \n[a] Yes \n[b] No \n ')
#   if res == 'a':
#     return get_drink_type()
#   elif res == 'b':
#     print('Okay')
#   else:
#     print_message()
#     return extra_drink()

coffee_bot()

