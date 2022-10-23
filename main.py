groceries = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

i=0

for n in groceries.items():

    x = []

    for m in n[1]:
        x.append(m.capitalize())
        i += 1
    print(f'Idę do {n[0].capitalize()}, kupuję tu następujące rzeczy: {x}')
print(f'W sumie kupuję {i} produktów')

#1
#2
#3