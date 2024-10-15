add_and_double = lambda x, y: (x + y) * 2

numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda x: x * 2, numbers))

for x in doubled_numbers:
    print(x)
