def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "division by zero is prohibited"
    except ValueError:
        return "enter only number"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))