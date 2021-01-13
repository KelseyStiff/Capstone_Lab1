classes = []
print('What classes are your taking?')
class_name = input('Enter class (press enter to quit): ')

while class_name:
    classes.append(class_name)
    class_name = input('Enter class (press enter to quit): ')

print('Your Spring semster classes are: ')
for index, c in enumerate(classes):
    print(f'{index+1} {c}')

    