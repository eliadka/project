my_list = ['test1\n','test234\n','test13\n']
with open('test1.txt', 'w+') as f_obj:
    f_obj.writelines(my_list)
with open('test1.txt') as f_obj:
    lines = 0
    letters = 0
    for line in f_obj:
        lines += line.count("\n")
        letters = len(line) - 1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")