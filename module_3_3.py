def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b=25)
print_params(c=[1, 2, 3])
value_list = [22, 'volume', False]
values_dict = {'a':31, 'b':32, 'c': 33}
print_params(*value_list)
print_params(**values_dict)
value_list2 = [54.32, 'Строка']
print_params(*value_list2,42)