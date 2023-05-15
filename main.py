my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Изначальный кортеж: ", my_tuple)
element_to_remove = int(input("Введите элемент, который хотите удалить: "))

if element_to_remove in my_tuple:
    new_tuple = tuple(i for i in my_tuple if i != element_to_remove)
    print("Новый кортеж: ", new_tuple)
else:
    print("Такого элемента нет в кортеже.")