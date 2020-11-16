from sys import argv
name, time, salary, bonus = argv

calculation = (int(time) * int(salary)) + int(bonus)
print(f"Your pay is equal {calculation}")