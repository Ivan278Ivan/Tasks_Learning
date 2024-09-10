immutable_var = 1,2, "a", "b"
print (immutable_var)
#immutable_var [0] = 2
# TypeError: 'tuple' object does not support item assignment
# Кортедж не поддерживает назначение элементов
Mutable_List = [1, 2, "a", "b"]
Mutable_List.append("Modified")
print(Mutable_List)
