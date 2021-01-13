sentence = input('enter string to convert: ' ).title()

word_list = sentence.split()

word_list_two = (''.join(word_list))

camel_case = sentence[0:1].lower() + word_list_two[1:]
print(camel_case)
