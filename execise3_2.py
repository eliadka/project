#Реализовать функцию, принимающую несколько параметров,
#описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Bystrova', name='Elena', year='1984', city='Spb', email='error@gmail.com',
              telephone='+7-911-323-49-23'))
