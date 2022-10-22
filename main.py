groceries = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
i=0
for n in groceries:
    x = []
    for m in groceries[n]:
        x.append(m.capitalize())
        i += 1
    print(f'Idę do {n.capitalize()}, kupuję tu następujące rzeczy: {x}')
print(f'W sumie kupuję {i} produktów')