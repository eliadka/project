from itertools import count, cycle
##################################
for i in count(start=1, step=1):
    # if i > 100:
    #    break
    print(i)

########################################
chandelier = ['switch on', 'switch off']

for chandelier in cycle(chandelier):
    print(chandelier)
