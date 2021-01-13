#asks for name and bday input
#prints welcome message, number of letters in name
#if bday is august prints happy bday message

name = input('Enter your name: ')
birthday_month = input('Enter your Birthday Month: ')

print(f'Hello and Welcome, {name}!')

if birthday_month.lower() == 'january':
    print(f'Happy Birthday {name}!')

print(f'There are {len(name)} letters in your name.')