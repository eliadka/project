my_int = 5
my_float = 1.3
my_str = 'Elena Bystrova'
my_list = ['Anna','Irina', True, 20, 30.2]
my_tuple = ('Anna','Irina', True, 20, 30.2)
my_set = {1, 2, 2, 3, 3, 6, 5, 6, 6, 7, 3, 4, 10}
my_dict = {'name': 'Elena', 'age': 36, 'female':'woman'}
full_list = [my_int, my_float, my_str, my_list, my_tuple, my_set, my_dict]

for i in full_list:
    print(f'{i} is {type(i)}')
