my_list = [37, 2, 3, 14, 5, 9, 7, 5, 4, 10]

print(f'Новый список {[num for num in my_list if num > my_list[my_list.index(num)-1]]}')
