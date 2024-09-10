grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_st = list(students) # множество в лист
list_st.sort() # сортировка списка
# print(list_st) проверка сортировки
klass = {(list_st[0]):(sum(grades[0])/len(grades[0])),
(list_st[1]):(sum(grades[1])/len(grades[1])),
(list_st[2]):(sum(grades[2])/len(grades[2])),
(list_st[3]):(sum(grades[3])/len(grades[3])),
(list_st[4]):(sum(grades[4])/len(grades[4]))}
print(klass)


