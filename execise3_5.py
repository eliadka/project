def my_func ():
    sum_result = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_result = sum_result + res
        print(f'Current sum is {sum_result}')
    print(f'Your final sum is {sum_result}')


my_func()