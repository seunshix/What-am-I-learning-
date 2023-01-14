# Write your code below: 
from contextlib import contextmanager

nl = '\n'

@contextmanager
def generic(card, sender, recipient):
  open_card = open(card, 'r')
  new_card = open(f'{sender}_generic.txt', 'w')

  try:
    new_card.write(f'Dear {recipient}, ' + nl)
    new_card.write(f'{open_card.read()}. {nl}')
    new_card.write(f'Sincerely, {sender} {{nl}}')
    yield new_card
  finally:
    open_card.close()
    new_card.close()

with generic('thankyou_card.txt', 'Eniola', 'Badmus') as open_file:
  print('Card Generated')

with open('Eniola_generic.txt', 'r') as file:
  print(file.readlines())

class Personalized:
  def __init__(self, sender, recipient):
    self.sender = sender
    self.recipient = recipient
    self.personalized = open(f'{self.sender}_personalized.txt', 'w')
  
  def __enter__(self):
    self.personalized.write(f'Dear {self.recipient} {nl}') 
    return self.personalized
  
  def __exit__(self, *exc):
    self.personalized.write(f'Sincerely')
    self.personalized.close()

with Personalized('John', 'Micheal') as file:
  file.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

print('-' * 30)

# with open('John_personalized.txt', 'r') as file:
#   print(file.readlines())

with generic('happy_bday.txt', 'Josiah', 'Remy') as file1,Personalized('Josiah', 'Esther') as file2:
  file2.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!")


