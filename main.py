print('Welcome to the Elite 101 Chatbot!')

name = input('Please enter your name: ')

age = int(input('Nice to meet you, ' + name + '! How old are you? '))

botAge = age * 10
loop = True

print()
print('Welcome, ' + name + '! I am ' + str(botAge) + ' years old.')
print('Oh to be ' + str(age) + ' again! How may I help you today?')
print()

while (loop): 
  print('Please choose from the following options:')
  print('1. Placeholder 1')
  print('2. Placeholder 2')
  print('3. Placeholder 3')
  print('4. Exit the conversation\n')
  
  num = int(input('Enter a number of your choice: '))
  print()

  if (num == 1):
    print('Placeholder 1\n')
  elif (num == 2):
    print('Placeholder 2\n')
  elif (num == 3):
    print('Placeholder 3\n')
  elif (num == 4):
    print('Goodbye, ' + name + '! Have a great day!')
    loop = False
  else:
    print('Invalid input. Please try again.\n')