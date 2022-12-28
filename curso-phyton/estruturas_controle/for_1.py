#! python

for i in range(1, 11):
    print('i = {}'.format(i))

for j in range(10):
    print(f'j = {j}')

for sla in range(1, 11):
    for vtmnc in range(1, 11):
        print(f'{sla} * {vtmnc} = {sla * vtmnc}')
