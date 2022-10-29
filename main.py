#Zadanie 1
groceries = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
count = 0
for n, value in groceries.items():
    print(f"Idę do {n.capitalize()} i kupuję tam {[item.capitalize() for item in value]}")
    if isinstance(value, list):
        count += len(value)


print(f'W sumie kupuję {count} produktów')

#Zadanie 2
x = range(0, 101)
print(f"{[n for n in x if n % 5 == 0]}")
print(f"{[n**3 for n in x if n % 5 == 0]}")
print(f" ")