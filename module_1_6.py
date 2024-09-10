# Словари и работа с ними.
my_dict = {'vasya': 1975, 'egor':1999, 'masha': 2002}
print (my_dict)
print (my_dict['vasya'])
print (my_dict.get('petr','нет во множестве'))
my_dict.update({'tatyana': 1971, 'yulia':1968})
print('Удаление переменной -', my_dict.pop('vasya'))
# print("Deleted: vasya")
print (my_dict)
# Множества
print()
my_set = {1, 1, 1.251, 1.251, 'pole', 'pole'}
print(my_set)
my_set.add('tt')
my_set.add((246,2,15))
my_set.discard(1)
print(my_set)